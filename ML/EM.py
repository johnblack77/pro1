from scipy import stats
import numpy as np

# 硬币投掷结果观测序列
observations = np.array([[1, 5, 8, 14, 22, 48, 50,58, 70 ,76,91, 95,96, 98, 107, 108,130,131, 132,134,136 ,139, 145 ,149],
                         [7 ,25, 40, 50, 56, 66, 70, 84, 93, 95, 117, 131, 132, 137, 141, 145, 149],
                         [3,8 ,13, 15, 18, 19, 37, 48, 53, 56, 57, 62, 64, 87, 92, 110, 118, 120, 137, 144, 146, 149],
                         [8, 11, 24, 56, 70, 72, 73, 87, 88, 91, 128, 129, 132,136, 137, 148],
                         [0, 7, 8, 11, 14, 18, 19, 51, 57, 59, 73, 87, 95, 107, 137, 149]])




def em_single(priors, observations):
    """
    EM算法单次迭代
    Arguments
    ---------
    priors : [theta_A, theta_B]
    observations : [m X n matrix]

    Returns
    --------
    new_priors: [new_theta_A, new_theta_B]
    :param priors:
    :param observations:
    :return:
    """
    counts = {'A': {'H': 0, 'T': 0}, 'B': {'H': 0, 'T': 0}}
    theta_A = priors[0]
    theta_B = priors[1]
    # E step
    for observation in observations:
        len_observation = len(observation)
        num_heads = observation.sum()
        num_tails = len_observation - num_heads
        contribution_A = stats.binom.pmf(num_heads, len_observation, theta_A)
        contribution_B = stats.binom.pmf(num_heads, len_observation, theta_B)  # 两个二项分布
        weight_A = contribution_A / (contribution_A + contribution_B)
        weight_B = contribution_B / (contribution_A + contribution_B)
        # 更新在当前参数下A、B硬币产生的正反面次数
        counts['A']['H'] += weight_A * num_heads
        counts['A']['T'] += weight_A * num_tails
        counts['B']['H'] += weight_B * num_heads
        counts['B']['T'] += weight_B * num_tails
    # M step
    new_theta_A = counts['A']['H'] / (counts['A']['H'] + counts['A']['T'])
    new_theta_B = counts['B']['H'] / (counts['B']['H'] + counts['B']['T'])
    return [new_theta_A, new_theta_B]


def em(observations, prior, tol=1e-6, iterations=10000):
    """
    EM算法
    :param observations: 观测数据
    :param prior: 模型初值
    :param tol: 迭代结束阈值
    :param iterations: 最大迭代次数
    :return: 局部最优的模型参数
    """
    import math
    iteration = 0
    while iteration < iterations:
        new_prior = em_single(prior, observations)
        delta_change = np.abs(prior[0] - new_prior[0])
        if delta_change < tol:
            break
        else:
            prior = new_prior
            iteration += 1
    return [new_prior, iteration]


if __name__ == "__main__":
    result = em(observations, [0.6, 0.4])
    print(result)

