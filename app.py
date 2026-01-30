
from flask import Flask, render_template, request
from currency import reduce_currency

app = Flask(__name__)

# Home route redirects to currency tool
@app.route('/')
def home():
    return render_template('currency_tool.html', active_page='currency')

# Currency Tool
@app.route('/currency', methods=['GET', 'POST'])
def currency_tool():
    result = None
    if request.method == 'POST':
        try:
            gold = int(request.form.get('gold', 0))
            silver = int(request.form.get('silver', 0))
            brass = int(request.form.get('brass', 0))
            reduction_type = request.form.get('reduction_type', 'percent')
            if reduction_type == 'amount':
                reduce_gold = int(request.form.get('reduce_gold', 0))
                reduce_silver = int(request.form.get('reduce_silver', 0))
                reduce_brass = int(request.form.get('reduce_brass', 0))
                result = reduce_currency(gold, silver, brass, None, reduce_gold, reduce_silver, reduce_brass)
            else:
                reduction = float(request.form.get('reduction', 0))
                result = reduce_currency(gold, silver, brass, reduction)
        except Exception:
            result = 'error'
    return render_template('currency_tool.html', result=result, active_page='currency')

# Placeholder Tool 2
@app.route('/tool2')
def tool2():
    return render_template('tool2.html', active_page='tool2')

# Placeholder Tool 3
@app.route('/tool3')
def tool3():
    return render_template('tool3.html', active_page='tool3')

if __name__ == '__main__':
    app.run(debug=True)
