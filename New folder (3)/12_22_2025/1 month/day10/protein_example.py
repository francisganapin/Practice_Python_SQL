from flask import Flask,request,jsonify
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


sales = []
sale_id_counter  = 1

@app.route('/api/sales',methods=['POST'])
def record_sale():

    global sale_id_counter

    data = request.get_json()

    required_fields = ['product_name','quantity','price_per_unit','customer_name','payment_method']
    for field in required_fields:
        if field not in data:
            return jsonify({'error':f'Missing field:{field}'}),400

    
    total_amount = data['quantity'] * data['price_per_unit']

    sale = {
        'sale_id':sale_id_counter,
        'product_name':data['product_name'],
        'quantity':data['quantity'],
        'price_per_unit':data['price_per_unit'],
        'customer_name':data['customer_name'],
        'payment_method':data['payment_method'],
    }

    sales.append(sale)
    sale_id_counter += 1

    return jsonify({
        'message':'Sale recorded successfully',
        'sale_id':sale['sale_id'],
        'total_amount':total_amount
    }),201

@app.route('/api/sales/count',methods=['GET'])
def get_sales():
    return jsonify(sales)


if __name__ == '__main__':
    app.run(debug=True)