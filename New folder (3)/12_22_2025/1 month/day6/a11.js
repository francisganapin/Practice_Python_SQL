let is_status = 'paid'

switch (is_status){
    case 'paid':
        console.log('Payment recieved');
        break;
    case 'pending':
        console.log('Await payment');
        break;
    default:
        console.log('Unknown status');
}