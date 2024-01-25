def calc_iva(price, iva):

    iva_to_apply = 21

    if iva is not None:
        iva_to_apply = iva

    print(f"price with and without tax | {price} : {(price * (iva_to_apply / 100)) + price}")    