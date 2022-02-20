from cutecharts.charts import Line
from cutecharts.charts import Bar
from cutecharts.components import Page
from cutecharts.faker import Faker

# cutecharts is specially used for the handwriting
def bar_vase() -> Bar:
    chart = Bar("Bar-cutecharts example 1")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    return chart


chart = Line('The sales of one market')
chart.set_options(
    labels=['shirt', 'sweater', 'tie', 'pants', 'windbreaker', 'high-heel', 'socks'],
    x_label="I'm xlabel",
    y_label="I'm ylabel"
)
chart.add_series("series-A", [5, 134, 137, 129, 145, 60, 49])
chart.add_series("series-B", [114, 55, 27, 101, 27, 105])
chart.render()

# from cutecharts.charts import Radar
# from cutecharts.components import Page
# from cutecharts.faker import Faker
#
#
# def radar_base() -> Radar:
#     chart = Radar("Radar-基本示例")
#     chart.set_options(labels=Faker.choose())
#     chart.add_series("series-A", Faker.values())
#     chart.add_series("series-B", Faker.values())
#     return chart
#
#
# radar_base().render()


# def radar_legend_colors():
#     chart = Radar("Radar-颜色调整")
#     chart.set_options(labels=Faker.choose(), colors=Faker.colors, legend_pos="upRight")
#     chart.add_series("series-A", Faker.values())
#     chart.add_series("series-B", Faker.values())
#     return chart
#
#
# page = Page()
# page.add(radar_base(), radar_legend_colors())
# page.render()
