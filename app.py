from flask import Flask, render_template, request, redirect
import requests
from bokeh.plotting import figure
from io import BytesIO
import os
from bokeh.embed import components
import pandas as pd


app = Flask(__name__)

app.vars = {}

plot_choices={'close':'close',    'adj_close':'adj_close',   'open':'open', 'adj_open':'adj_open'}
plot_colors={0:'blue',1:'red',2:'green',3:'magenta'}
@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('stock_info.html')
    else:
        for key in request.form.keys():
            app.vars[key] = request.form[key]
        return redirect('/result')

@app.route('/result', methods=['GET', 'POST'])
def result():

    
    stock_ticker = app.vars['stock_ticker']
    api_url='https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?api_key=YwxVxgpgdavvx-E3dYFe&ticker=%s' %stock_ticker
    session = requests.Session()
    session.mount('http://',requests.adapters.HTTPAdapter(max_retries=3))
    raw_data=session.get(api_url)
    rel_data=raw_data.json()['datatable']
    df1 = pd.DataFrame(data = rel_data['data'],
                       columns = [col['name'] for col in rel_data['columns']], )

    df1['date']=pd.to_datetime(df1['date'])
    df1=df1.sort_values(by='date',ascending=False)
    
    
    plot=figure(tools="pan,wheel_zoom,box_zoom,reset,save",
                title='Data from Quandle WIKI set',
                x_axis_label='date',
                x_axis_type='datetime')
    #we want to access to the other variables so we need to remove stock_ticker from it
    #to be able to iterate
    del app.vars['stock_ticker']

    for i, key in enumerate(app.vars.keys()):
        plot.line(df1['date'],df1[plot_choices[key]],legend='{0}:{1}'.format(stock_ticker,plot_choices[key]),
                  color=plot_colors[i])
    
    script, div = components(plot)

    return render_template('stock_result.html', script=script, div=div)


###################################################################################

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 33507))
    app.run(port=33507)
