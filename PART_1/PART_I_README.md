# 📝 PART 1: Underground Cables —— Time-Varying Risk and Chronic Degradation Auditing

## 📄 Manuscript PDF ([PDF Download](./part_I_From_Causal_Auditing_to_Value_Maximization_for_Core_Distribution_Assets—Underground_Cable_Management.pdf))
*   **Release Date**: 2026-06-13

## 📌 Methodology Heritage
This research is not merely an independent exploration of underground cables, but a deep integration and cross-domain migration of two top-level framework concepts. This ensures high academic consistency across the series and maintains the coherent foundation of the "Bianque System":

> 🌊 **1. Migration from: Zeng, Y. (2026). *From Causal Auditing to Value Maximization...*** (Offshore Wind Asset Management Guidelines)
> *   **[Micro-Fingerprint Tracking ➡️ Time-varying Covariates]**: Discarding macro-level coarse data and drawing on the approach of extracting "0.3% precision manufacturing deviations" in offshore wind, this study extracts highly microscopic electromagnetic fingerprints such as high-frequency partial discharge (PD) and dielectric loss (tan δ) of cables as core model inputs (time-varying covariates).
> *   **[White-Box Causal Auditing ➡️ Physical Mechanism Reverse Engineering]**: Adhering to the pure white-box spirit and avoiding blind reliance on black-box deep learning. Through the competitive auditing of statistical distribution models, the physical degradation mechanism of water tree aging is reversely inferred (Causal Auditing).
> *   **[Optimal Stopping Theory ➡️ Value Maximization]**: Directly reusing the "Optimal Stopping Theory" and "Dual-Redline Mechanism" proven in offshore wind to translate the predicted survival probability $S(t)$ into economic decisions for the optimal timing of trenching and cable replacement, ultimately realizing Value Maximization.

> 🔍 **2. Migration from: Shadi et al. (2026). *Survival Models for Predictive Maintenance...*** (Review of Survival Models in Smart Energy Networks)
> *   **[6-Mirror Panel Auditing Mechanism]**: Based on the multi-parameter survival model auditing framework provided by this review, a "6-Mirror Panel" is systematically constructed, ranging from semi-parametric (Cox), fully parametric (Weibull/Lognormal) to machine learning (RSF), to comprehensively combat complex right-censoring data.
> *   **[Non-stationary Factor Processing]**: Adopting the advanced survival modeling techniques for time-varying covariates proposed in the literature to precisely capture the highly time-dependent risks of the "chronic disease" in cables.

---

## 1. 💡 Idea / Concept
**Core Concept: Treating the insulation degradation of underground cables as a "chronic disease".**
During long-term buried operation, the complete failure (insulation breakdown) of a cable is rarely sudden. Instead, it is a long-term, chronic process of corrosion and degradation driven by the intertwining of multiple **non-stationary factors** such as temperature, humidity, and electrical load.

**Breakthrough Point: Introducing medical-grade Survival Analysis.**
Traditional life prediction often relies on simplistic assumptions of fixed degradation rates. This study aims to break this crude physical black box. By leveraging the "etiological traceability" mindset from the medical field, we examine how long-latent "pathogens" (e.g., water tree aging) non-linearly erode the survival probability of the cable step by step.

## 2. 🎯 Research Objective
*   **Time-varying Risk Auditing**: Focusing on how dynamic micro-fingerprints (time-varying covariates) that change over time, such as water tree aging and partial discharge, dynamically affect the breakdown (death) probability of the cable.
*   **Hypothesis Testing & Physical Mechanism Reverse Engineering**: Challenging the traditional distribution models commonly used in academia. We will verify: Under complex physical mechanisms like water tree aging, has the conventional Weibull distribution failed? Which survival curve perfectly aligns with this "chronic disease mechanism"?

## 3. 🛠️ Methodology
Following the principle of "Data-Driven Model Selection":

### Step 1: Data Integration & Micro-Fingerprint Extraction
*   **Feature Extraction**: Integrating sensor data such as high-frequency PD intensity to extract microscopic **time-varying covariates** that reflect degradation characteristics.
*   **Censoring Processing**: Utilizing the unique censoring mechanisms of survival analysis to handle massive amounts of **right-censored data**.

### Step 2: 6-Mirror Model Panel Auditing
*   Constructing a "racing panel" containing six survival algorithms:
    *   Semi-parametric: Classical Cox Proportional Hazards Model (Cox-PH)
    *   Fully parametric: Weibull, Lognormal, Exponential, Accelerated Failure Time (AFT) models
    *   Non-linear: Survival Random Forests (RSF) or Gradient Boosting Survival Trees.

### Step 3: White-Box Causal Auditing & Value Maximization Decision-Making
*   **Causal Auditing**: Through the statistical distribution of the winning model (e.g., if Lognormal wins, it signifies cumulative multiplicative effects), reversely explaining the non-linear accelerated physical effects of water tree aging.
*   **Value Maximization**: Substituting the survival probabilities derived from the optimal curve into the **Optimal Stopping Theory** equations to calculate the optimal economic redline point for "live-line detection vs. complete replacement".

## 4. 🚀 Expected Outcomes
*   **An Operational Algorithm Pipeline**: Capable of receiving microscopic time-series sensor data in real-time and outputting individualized dynamic survival probability curves for cables.
*   **A Core Academic Conclusion**: Providing strong data-driven evidence that a specific survival model (such as Lognormal or RSF) is far superior to the traditional Weibull distribution in revealing the physical mechanism of water tree aging in underground cables.
*   **An Economic Decision Engine**: Providing power grid asset managers with intervention redlines based on "Optimal Stopping Theory," achieving an ultimate commercial balance between downtime risk aversion and budget efficiency.

## 📂 Directory Structure
*   **[`data/`](./data/)**: Contains experimental data, desensitized high-frequency partial discharge (PD), and dielectric loss sensor feature data used for survival analysis model training and evaluation.
*   **[`figures/`](./figures/)**: Contains all illustrations, survival curve comparisons, and visualization results used in the manuscript.
*   **[`scripts/`](./scripts/)**: Contains the core Python algorithmic scripts for data preprocessing, 6-Mirror panel auditing (Cox/Weibull/RSF, etc.), and manuscript figure generation.


---
*"The superior doctor prevents sickness." —— The Bianque System: Auditing causality with data, foreseeing the future with algorithms.*

---

## 🙌 Acknowledgements
In exploring the underlying survival algorithms for predictive maintenance of distribution network assets, this research was profoundly inspired by the team of **M. R. Shadi, H. Mirshekali, M. Tahavori, and H. R. Shaker** [1]. Their comprehensive review article provided a valuable taxonomic framework and theoretical guidance for survival models in sensor-enabled smart energy networks, laying a solid foundation for the "6-Model Panel Diagnosis" and algorithm selection mechanism of the Bianque System. We hereby express our most sincere respect and gratitude to their team.

---

## 📚 References
[1] Shadi, M. R., Mirshekali, H., Tahavori, M., & Shaker, H. R. (2026). Survival Models for Predictive Maintenance and Remaining Useful Life in Sensor-Enabled Smart Energy Networks: A Review. *Sensors*, 26(6), 1915. https://doi.org/10.3390/s26061915
[2] Zeng, Y. (2026). From Causal Auditing to Value Maximization: Individualized Management Guidelines for Offshore Wind Assets (v1.0.0). *Zenodo*. https://doi.org/10.5281/zenodo.20391481
