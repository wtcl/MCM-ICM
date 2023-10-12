from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker

a=[list(z) for z in zip(Faker.choose(), Faker.values())]
print(a)
c = (
    Funnel()
    .add(
        "商品",
        a,
        sort_="ascending",
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图"))
    .render()
)