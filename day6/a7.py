status = 'paid'


match status:
    case 'paid':
        print('Payment Recieve')
    case 'pending':
        print('Awaiting payment')
    case _:
        print('Unknown satus')