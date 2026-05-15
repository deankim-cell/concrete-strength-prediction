import threading
from flask import Flask, render_template, request, jsonify
from concrete_data import (get_recommendation, BUILDING_BASE, USE_CASES,
                           MEMBER_NAMES, MATERIAL_INFO, REGIONS)
import ml_model

app = Flask(__name__)

threading.Thread(target=ml_model.initialize, daemon=True).start()


@app.route("/")
def index():
    return render_template(
        "index.html",
        buildings=BUILDING_BASE,
        use_cases=USE_CASES,
        members=MEMBER_NAMES,
        materials=MATERIAL_INFO,
        regions=REGIONS,
    )


@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json(silent=True) or {}

    # Pull custom prices if provided by the user
    custom_prices = data.get("prices") or None

    result = get_recommendation(
        building_type=data.get("building_type", "residential"),
        floors=int(data.get("floors", 5)),
        use_case=data.get("use_case", "general_indoor"),
        member=data.get("member", "slab"),
        custom_prices=custom_prices,
    )

    ml_strength = ml_model.predict(
        cement=result["cement_kg"],
        slag=result["slag_kg"],
        flyash=result["flyash_kg"],
        water=result["water_kg"],
        superplasticizer=result["sp_kg"],
        coarseagg=result["coarseagg_kg"],
        fineagg=result["fineagg_kg"],
        age=28,
    )

    result["ml_predicted_strength"] = ml_strength
    result["ml_model_ready"]        = ml_model.is_ready()
    result["ml_error"]              = ml_model.get_error()

    # Cost efficiency: MPa per $10 USD
    if ml_strength and result["total_cost"] > 0:
        result["cost_efficiency"] = round(ml_strength / result["total_cost"] * 10, 2)
    else:
        result["cost_efficiency"] = None

    return jsonify(result)


@app.route("/api/region-prices/<region_key>")
def region_prices(region_key):
    from concrete_data import REGIONS
    region = REGIONS.get(region_key)
    if not region:
        return jsonify({"error": "Unknown region"}), 404
    return jsonify(region["prices"])


@app.route("/api/model-status")
def model_status():
    return jsonify({"ready": ml_model.is_ready(), "error": ml_model.get_error()})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
