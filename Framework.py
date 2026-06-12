import numpy as np


# ----------------------------
# 1. Risk Weights
# ----------------------------
def compute_risk_weights(risk_params):
    R = {
        o: p["lambda"] * p["iota"] * p["epsilon"] * p["assurance"] * p["localization"]
        for o, p in risk_params.items()
    }
    total = sum(R.values())
    return {o: (R[o] / total if total else 1 / len(R)) for o in R}


# ----------------------------
# 2. Base Effectiveness
# ----------------------------
def compute_base_eta(topics, objectives, r, u, v, beta):
    eta = {}
    for t in topics:
        for o in objectives:
            eta[(t, o)] = beta * r.get((t, o), 0) + (1 - beta) * v.get(t, 0) * u.get((t, o), 0)
    return eta


# ----------------------------
# 3. Interdependency Adjustment
# ----------------------------
def compute_adjusted_eta(topics, objectives, eta, D, alpha):
    idx = {t: i for i, t in enumerate(topics)}
    n = len(topics)

    M = np.eye(n)
    for (ti, tj), val in D.items():
        if ti in idx and tj in idx:
            M[idx[ti], idx[tj]] += alpha * val

    eta_mat = np.array([[eta.get((t, o), 0) for o in objectives] for t in topics])
    eta_prime = M @ eta_mat

    return {
        (topics[i], objectives[j]): eta_prime[i, j]
        for i in range(len(topics))
        for j in range(len(objectives))
    }


# ----------------------------
# 4. Final Scoring
# ----------------------------
def compute_scores(topics, objectives, eta_prime, weights):
    return {
        t: sum(weights[o] * eta_prime[(t, o)] for o in objectives)
        for t in topics
    }


def rank_topics(scores):
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":

    objectives = ["Av", "Phy", "AM", "CIA"]

    topics = [
        "Network Security",
        "IAM",
        "Cryptography",
        "Security Operations",
        "Awareness",
        "Critical Infrastructure",
        "Threat Intelligence",
        "Risk Analysis",
        "Physical Security",
        "Supply Chain"
    ]

    # Example inputs (replace with user input later)
    risk_params = {
        "Av": {"lambda": 0.4, "iota": 1, "epsilon": 1, "assurance": 0.7, "localization": 0.5},
        "Phy": {"lambda": 0.4, "iota": 0.7, "epsilon": 1, "assurance": 0.7, "localization": 0.5},
        "AM": {"lambda": 0.6, "iota": 0.5, "epsilon": 0.7, "assurance": 0.7, "localization": 0.5},
        "CIA": {"lambda": 0.7, "iota": 0.4, "epsilon": 0.6, "assurance": 0.7, "localization": 0.5},
    }

    weights = compute_risk_weights(risk_params)

    # (you will plug r, u, v, D from user input or config)
    r, u, v, D = {}, {}, {}, {}

    beta = 0.7
    alpha = 0.2

    eta = compute_base_eta(topics, objectives, r, u, v, beta)
    eta_prime = compute_adjusted_eta(topics, objectives, eta, D, alpha)

    scores = compute_scores(topics, objectives, eta_prime, weights)
    ranking = rank_topics(scores)

    print("Ranking:")
    for i, (t, s) in enumerate(ranking, 1):
        print(f"{i}. {t}: {s:.4f}")
