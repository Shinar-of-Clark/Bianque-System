# 📝 PART 2: Switchgear / Circuit Breakers —— Dynamic Retirement & Precision Life Extension via RUL Auditing

> 🔙 **Navigation:** [Back to Bianque System Roadmap](../readme.md) | ⏪ [Previous: PART 1 (Underground Cables)](../PART_1/PART_I_README.md)

## 📄 Manuscript PDF ([PDF Download](./paper_2_draft_V1_EN.pdf))
*   **Status**: Work in Progress
*   **Target Equipment**: Switchgear Family (AIS & GIS)
    *   *(Note: This research breaks the narrow barriers of traditional voltage levels, directly penetrating to the physical essence, and categorizing based on "insulation and arc-extinguishing medium". AIS represents an air-insulated system dominated by mechanical spring fatigue, while GIS represents a sealed chemical-insulated system dominated by SF6 gas leakage. This framework aims to build a universal auditing paradigm applicable to core switchgear assets across all voltage levels in the power grid.)*

### 📢 Evolution of Research Scope
*   **[2026-06-15] High-Voltage Clearance Boundary & "Tale of Two Cities" Dual-Track Architecture**
    *   **Scope Refinement**: This framework explicitly restricts the auditing target to core primary assets (AIS and GIS) that require **High-Voltage Clearance / Isolation** to execute maintenance, completely focusing on operational interventions with extremely high downtime costs.
    *   **"Tale of Two Cities" Dual-Track Architecture**: Breaking the limitation of a single piece of equipment, this research conducts auditing on two core switchgear assets synchronously and in parallel. Although the degradation of equipment in the real world is multi-dimensional (e.g., insulation aging, contact burnout), this system adheres to the "Weakest Link Effect" principle. It extracts the **most fatal physical fingerprints** that determine retirement and replacement for AIS and GIS respectively, serving as the input standards for the survival algorithms:
        *   **👉 AIS Auditing Standard (Dominance of Mechanical Fatigue)**: Although AIS is exposed to the air, power grid big data shows that over 70% of its major faults and ultimate retirements stem from the aging and jamming of the heavy spring mechanical operating mechanism. Therefore, this system selects **closing/opening coil current delay and spring energy storage time** as its core degradation indicators, precisely capturing its non-monotonic physical wear trajectory that exhibits "Mid-Life Crisis" characteristics.
        *   **👉 GIS Auditing Standard (Fatality of Gas Leakage)**: GIS isolates external environmental dust through a fully enclosed architecture, minimizing mechanical transmission risks. However, its "Achilles' heel" lies in SF6 gas micro-leakage caused by rubber seal aging. Once the gas pressure drops below the arc-extinguishing threshold, the equipment instantly faces catastrophic destruction. Therefore, this system selects **SF6 pressure drop rate and micro-water content increment** as core degradation indicators to reveal its monotonic and irreversible chemical deterioration laws.
        *   *(Conclusion: This separated yet synchronous analysis will powerfully prove to the academic community: Even within the same broad family (switchgear), the system can adaptively use completely different survival models to precisely capture the huge physical chasm behind these two types of equipment.)*
    *   **Out-of-Scope Acknowledgment**: Although **SIS (Solid Insulated Switchgear)**, representing the future environmental protection trend, is gradually rising, considering its actual installed capacity in the whole grid is still small, this research temporarily places it on the observation list. This paper only discusses AIS and GIS, which currently hold absolute dominance in the power grid.

## 📌 Methodology Heritage
This research is not merely an independent exploration of switchgears, but a deep integration and cross-domain synergy of top-level industrial architecture ecosystems. This ensures extremely high academic consistency across the entire series, and macroscopically completes the puzzle of the two major industrial diagnostic systems (Bianque and Laplace) under the author's name:

> 🌊 **1. Paradigm Inheritance**: Zeng, Y. (2026). *From Causal Auditing to Value Maximization: Individualized Management Guidelines for Offshore Wind Assets*. Zenodo. [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20391481-blue)](https://doi.org/10.5281/zenodo.20391481)
> *   **[Micro-Fingerprint Tracking ➡️ Mechanical Fatigue Covariates]**: Discarding macro-level coarse data like "calendar age", this study extracts highly microscopic mechanical fingerprints—such as closing/opening coil current delay, spring energy storage time, and contact resistance—as core model input variables.
> *   **[White-Box Causal Auditing ➡️ Physical Mechanism Reverse Engineering]**: Adhering to the pure white-box spirit. By letting multiple models compete (racing), we reversely infer the non-monotonic physical degradation mechanism of mechanical springs and linkage systems (e.g., the "Mid-Life Crisis" phenomenon).
> *   **[Optimal Stopping Theory ➡️ Value Maximization]**: Translating the predicted Remaining Useful Life (RUL) into a dynamic economic redline, precisely answering *when* to execute a "mid-life overhaul" (e.g., replacing only the VCB truck while keeping the cabinet) to achieve a Value Reset.

> 🔍 **2. Taxonomy Reference**: Shadi, M. R., Mirshekali, H., Tahavori, M., & Shaker, H. R. (2026). *Survival Models for Predictive Maintenance and Remaining Useful Life in Sensor-Enabled Smart Energy Networks: A Review*. Sensors, 26(6), 1915. [![DOI](https://img.shields.io/badge/DOI-10.3390%2Fs26061915-green)](https://doi.org/10.3390/s26061915)
> *   **[6-Mirror Panel Auditing Mechanism]**: Systematically running a "racing panel" (Cox, Weibull, Lognormal, Log-logistic, Exponential, RSF) for every single piece of equipment to fairly and comprehensively combat complex right-censoring data.
> *   **[Non-stationary Factor Processing]**: Utilizing advanced survival modeling to precisely capture the highly time-dependent high-risk features in dynamic mechanical wear.

> ⚡ **3. Ecosystem Synergy**: Zeng, Y. (2026). *Mitigating Large Language Model Hallucinations in Industrial Environments via Asymmetric Deterministic Override Architecture*. Zenodo. [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20539607-orange)](https://doi.org/10.5281/zenodo.20539607)
> *   **[Dual-Engine Industrial Ecosystem Closed-Loop]**: Explicitly defined the scientific capability boundary of industrial auditing. The *Bianque System* focuses on **long-term gradual Degradation Failures** with physical degradation trajectories in this framework; while for **extremely short-term Catastrophic Failures** that cannot be predicted, such as instantaneous insulation breakdown and extreme overload, they are automatically stripped out and handed over to the homologous *Laplace Platform*, where its "Asymmetric Deterministic Override Architecture" performs transient capture and causal alignment. The two form a seamless interlocking ecosystem of "Bianque treating diseases before they occur" and "Laplace investigating acute emergencies".

## 💎 Core Value: Beyond Traditional Thresholds
In the industry, acquiring equipment status data through external sensors is no longer new, but traditional systems universally adopt a **"single dead threshold"** (e.g., alarming immediately when air pressure is below 0.4MPa or spring energy storage times out). This model has a fatal economic flaw: it is essentially **"collecting corpses for equipment"**. When the alarm is triggered, it often means that a high-risk hidden danger has already formed, damage to the equipment may have already been caused, and one is forced to face extremely expensive emergency unplanned outages and production line paralysis.

The soul of this *Bianque System* lies in **"treating diseases before they occur and calculating economic accounts"**, completely bridging the closed loop from underlying hardware sensors to high-level commercial decision-making:
1. **From "Passive Firefighting" to "Active Prediction"**: The system does not wait for data to touch the red line, but uses extremely cheap non-invasive online data (like micro-current waveforms based on secondary control loops) to acutely capture the degradation slope through survival analysis, accurately reverse-deducing the critical day of equipment collapse months in advance (e.g., "The system calculates that this GIS will touch the arc-extinguishing pressure bottom line in 43 days").
2. **From "Rough Line Drawing" to "Individualized Medical Treatment"**: Discarding the one-size-fits-all rigid thresholds across the network. The system introduces Time-varying covariates, considering non-stationary factors such as specific action frequencies and harsh environment exposure for each equipment, customizing a unique remaining life curve for every heavy asset.
3. **From "Blind Repair/Replacement" to "Optimal Return on Investment (ROI)"**: The system ultimately feeds the generated survival curve into the partial differential equations of the Optimal Stopping Theory. It precisely balances the "tens of thousands of yuan in planned repair/replacement costs" against "millions of yuan in sudden tripping penalties", ultimately outputting an instruction with absolute commercial certainty to the operator: **"Accurately lock in the issuance of the high-voltage blackout isolation work ticket at this moment to maximize ROI"**.

---

## 1. 💡 Idea / Core Concept
**Core Concept: Shifting from "Calendar-Based Population Management" to "Data-Driven Individualized Management".**
Traditional distribution grid management relies on a rigid "15-year forced replacement" rule. This causes massive CapEx waste by prematurely forcing healthy old equipment into retirement, while suffering catastrophic OpEx losses when heavily loaded young equipment fails early.

**Breakthrough Point: Deconstructing the "Older = Riskier" Myth into Dual-Track Physical Laws.**
Traditional operations widely believe the single rule that "the older the equipment, the easier it breaks", but under the "Tale of Two Cities" architecture of this study, we will reveal two entirely different physical truths:
1. **AIS "Mid-Life Crisis" (Non-Monotonic Law)**: The fatigue of heavy mechanical operating mechanisms does not rise in a straight line, but exhibits an **"Inverted U-shaped hazard rate"**. If an AIS safely passes its high-risk break-in and mid-life fatigue periods, its later operation can actually stabilize.
2. **GIS "Irreversible Aging" (Monotonic Law)**: In contrast, the chemical aging of rubber seals and gas tightness systems relied upon by GIS is relentlessly and continuously deteriorating, exhibiting a standard **"monotonically increasing hazard rate"**. The older the equipment, the absolutely higher the probability of instantaneous disaster caused by gas leakage.

## 2. 🎯 Research Objective
*   **Individualized RUL Auditing**: Generating a unique, customized dynamic survival probability curve for each asset based on its specific operational history (mechanical action frequency for AIS or pressure/micro-water variation for GIS).
*   **Hypothesis Testing & Physical Mechanism Reverse Engineering**: Challenging traditional "one-size-fits-all" modeling approaches. We will verify in massive dataset panel racing:
    *   Expecting non-linear models like **Log-logistic** to win out in the AIS population, mathematically proving the "Mid-Life Crisis" of mechanical operations.
    *   Expecting the classic **Weibull** distribution to take the top spot in the GIS population, mathematically corroborating the "monotonic continuous deterioration" of chemical seal aging.
    *(This proves that the Bianque System can automatically reverse-infer completely different underlying physical laws from raw data without manual preset!)*
*   **Dynamic Retirement & Precision Life Extension**: Providing absolute mathematical proof to safely extend the life of healthy aging switchgear (saving CapEx) and accurately target degrading young switchgear for early intervention (saving OpEx).

## 3. 🛠️ Methodology
Following the principle of "Data-Driven Model Selection":

### Step 1: Data Integration & Micro-Fingerprint Extraction
*   **Feature Extraction**: Integrating secondary side data such as VCB closing/opening time and coil current waveforms that can be obtained without power outages, extracting microscopic **time-varying covariates** reflecting mechanical fatigue.
*   **Censoring Processing**: Utilizing the unique censoring mechanisms of survival analysis to handle massive amounts of **right-censored** data from switchgear populations.

### Step 2: 6-Mirror Model Panel Auditing
*   Constructing a "racing panel" containing six survival algorithms:
    *   Semi-parametric: Classical Cox Proportional Hazards Model (Cox-PH)
    *   Fully parametric: Weibull, Lognormal, Exponential, Log-logistic models
    *   Non-linear: Survival Random Forests (RSF)
*   **Strict Adherence to Fairness**: The system NEVER assumes a model beforehand. All 6 models must compete based on Brier Score and C-index for every dataset diagnosis.

### Step 3: White-Box Causal Auditing & Value Maximization Decision-Making
*   **Causal Auditing**: Through the statistical distribution of the winning model (e.g., Log-logistic dominating across hundreds of switchgears), reversely proving the non-linear "rise-then-fall" physical effects of mechanical wear.
*   **Value Maximization**: Substituting the survival probabilities into the **Optimal Stopping Theory** equations to calculate the optimal economic point for "Retrofitting/Truck Replacement vs. Complete Cabinet Replacement".

### Step 4: Dynamic Calibration via P-F Interval (10-Decile Soft-Thresholds)
*   **"Trust Anchor" for Industrial Deployment**: In extremely conservative power grid environments, waiting for an asset to truly breach the functional death redline (**F-point** - Functional Failure, e.g., 0.4MPa total scrapping) to validate the algorithm is extremely dangerous and lengthy. Meanwhile, making distant predictions in the first half of the equipment's life cycle is often full of noise and lacks economic significance.
*   **Dual-Trigger P-Point (Potential Failure)**: This framework pioneers a "data + time" dual insurance trigger mechanism to define the P-point (potential failure starting point, i.e., the awakening moment of the prediction program):
    1.  **Data-Driven (Mutation Point Detection)**: The system has built-in CUSUM (Cumulative Sum) and 3-Sigma control charts. When the deviation value of degradation data statistically explicitly overshadows daily environmental noise, the algorithm immediately precisely locks the P-point.
    2.  **Time-Bottoming (Preventing Cliff-like Sudden Death)**: To prevent certain equipment from experiencing sudden death with an "extremely short P-to-F interval" after extreme stability, the system forcibly awakens the high-frequency prediction program when the equipment reaches **half of its conventional calendar life (Half-Life)**. Even if current data is calm, microscope monitoring mode must be activated.
*   **10-Decile Calibration & Dual-Boundary**: After crossing the P-point, the system strictly divides the residual space between the current state and the F-point death redline into 10 soft-threshold grades, executing the following advanced closed-loop:
    1.  **9 Dynamic Precision Approximations**: The algorithm continuously predicts the time to reach the next grade, utilizing actual arrival data to perform 9 Bayesian Updatings, allowing the prediction error funnel to converge exponentially and sharply.
    2.  **Dynamic Economic Boundary (Grades 1~8 Assessment)**: At every node crossing grades 1~8, the system recalculates the "Optimal Stopping Theory" equation in real-time. Once the ratio of "benefits from squeezing asset residual value" to "replacement cost" reaches a mathematical extremum, the system immediately issues a value-maximizing retirement and replacement instruction.
    3.  **Absolute Safety Boundary (Grade 9 Forced Fuse)**: Since the macro purpose of the *Bianque System* is "value maximization" rather than destructive death experiments, the algorithm absolutely does not allow equipment to run to the 10th grade (F-point true death). Once degradation touches the 9th grade, even if the economic formula shows remaining value, the system will immediately trigger forced isolation and replacement instructions.
    *(Conclusion: This design of "process relies on economic accounting, bottom line relies on 9th-grade fuse" not only achieves algorithm self-verification up to 9 times, but also completely drains the last commercial value of heavy assets under the premise of absolute zero risk.)*

## 4. 🚀 Expected Outcomes
*   **An Operational Algorithm Pipeline**: Capable of receiving mechanical sensor data and outputting individualized dynamic survival probability curves for switchgears.
*   **A Core Academic Conclusion**: Providing strong data-driven evidence that the Log-logistic distribution is far superior to the traditional Weibull distribution in revealing the physical mechanism of MV Vacuum Switchgears.
*   **An Economic Decision Engine**: Providing power grid asset managers with intervention redlines for **Precision Life Extension and Dynamic Retirement**, achieving the ultimate commercial balance.

## 📂 Directory Structure
*   **[`data/`](./data/)**: Contains experimental data, desensitized mechanical operation logs, and time-varying covariates for survival analysis.
*   **[`figures/`](./figures/)**: Contains all illustrations, survival curve comparisons (showcasing the Log-logistic victory), and economic intervention thresholds.
*   **[`scripts/`](./scripts/)**: Contains the core Python algorithmic scripts for data preprocessing, 6-Mirror panel auditing, and results generation.

---
*"The superior doctor prevents sickness." —— The Bianque System: Auditing causality with data, foreseeing the future with algorithms.*
