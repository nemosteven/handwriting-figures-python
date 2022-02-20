# 2022年02月18日 15:47

# 必须在jupyter-notebook中使用，其中完整的包名为py-roughviz
from roughviz.charts import Line
import pandas as pd


line = Line(data='vis1.csv', y1='a', y2='b', y3='c')
line.set_legend(legend_position='left')
line.set_title('Line Plot', fontsize=2)
line.set_options(colors=['tan', 'orange', 'coral'])

line.show()
