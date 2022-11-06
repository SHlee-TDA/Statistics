#-----------------------------------------------------
# P(A|B) = P(B|A)*P(A)/P(B) = P(B|A)*P(A)/[P(B|A)P(A) + P(B|not A)P(not A)]
#-----------------------------------------------------

# calculate P(A|B) given P(A), P(B|A), P(B|not A)
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    # calculate P(not A)
    p_not_a = 1 - p_a
    # calculate P(B)
    p_b = p_b_given_a*p_a + p_b_given_not_a*p_not_a
    # calculate P(A|B)
    p_a_given_b = p_b_given_a*p_a/p_b
    return p_a_given_b
