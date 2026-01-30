from flask import Flask, render_template, request

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
            reduction = float(request.form.get('reduction', 0))
            # Convert all to brass
            total_brass = gold * 240 + silver * 12 + brass
            # Apply reduction
            reduced_brass = int(total_brass * (1 - reduction / 100))
            # Convert back: at least 20 brass, at least 10 silver, rest gold, remainder as brass
            # First, check if we have enough for minimums
            min_brass = 20
            min_silver = 10
            needed_for_minimums = min_brass + min_silver * 12
            if reduced_brass < needed_for_minimums:
                # Not enough for minimums, allocate as much as possible
                silver_out = reduced_brass // 12
                brass_out = reduced_brass % 12
                gold_out = 0
            else:
                # Allocate minimums
                brass_out = min_brass
                silver_out = min_silver
                remaining = reduced_brass - (min_brass + min_silver * 12)
                # Allocate as much gold as possible
                gold_out = remaining // 240
                remaining = remaining % 240
                # Any remainder goes to brass
                brass_out += remaining
            result = {
                'gold': gold_out,
                'silver': silver_out,
                'brass': brass_out
            }
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
