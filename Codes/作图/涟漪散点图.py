from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker

print(Faker.choose())
print(Faker.values())
c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例",pos_right='40%'))
    .render()
)