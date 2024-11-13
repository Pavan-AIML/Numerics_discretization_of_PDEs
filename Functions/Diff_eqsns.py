def diff_b(b, r, lambda_b: int, r_e:int):
    f = lambda_b * b*(1-(r/r_e))
    return f


def diff_r(b,r,lambda_r:int, b_e:int):
    f = lambda_r * r * ((b/b_e) -1 )
    return f


def diff_b_modified_Euler(b,r,lambda_b:int, b_e:int,r_e:int,lambda_r :int, step_size:float):
    f = diff_b((diff_b(b, r,lambda_b, r_e)*step_size*0.5 + b), ((diff_r(b,r,lambda_r, b_e)*step_size*0.5 )+r), lambda_b, r_e)
    return f

def diff_r_modified_Euler(b,r,lambda_b:int, b_e:int,r_e:int,lambda_r :int, step_size:float):
    f = diff_r((diff_b(b, r,lambda_b, r_e)*step_size*0.5 + b), ((diff_r(b,r,lambda_r, b_e)*step_size*0.5 )+r), lambda_r, b_e)
    return f



