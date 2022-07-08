

class Line:
    def __init__(self, title: str, x: list, y: list, labels: list, legend: bool = False, area: bool = False):
        self.title = title
        self.x = x
        self.y = y
        self.labels = labels
        self.legend = legend
        self.area = area

    def plot(self):
        legend = {
            "data": self.labels,
            "show": self.legend,
            "top": "10%"
        }

        if self.area:
            series = [{
                "name": i[1],
                "data": self.y[i[0]],
                "type": "line",
                "areaStyle": {},
                "symbol": "none"
            } for i in enumerate(self.labels)]
        else:
            series = [{
                "name": i[1],
                "data": self.y[i[0]],
                "type": "line",
                "symbol": "none"
            } for i in enumerate(self.labels)]
        
        option = {
            "title":{"text": self.title},
            "legend": legend,
            "tooltip":{"trigger": "axis"},
            "xAxis": {
                "type": "category",
                "data": self.x
            },
            "yAxis": {"type": "value"},
            "series": series
        }

        return option

class Bar:
    def __init__(self, title: str, x: list, y: list, labels: list, legend: bool = False, orientation: str = "horizontal"):
        self.title = title
        self.x = x
        self.y = y
        self.labels = labels
        self.legend = legend
        self.orientation = orientation

    def plot(self):
        legend = {
            "data": self.labels,
            "show": self.legend,
            "top": "10%"
        }
        series = [{
            "name": i[1],
            "data": self.y[i[0]],
            "type": "bar",
            "symbol": "none"
        } for i in enumerate(self.labels)]
        
        if self.orientation == "horizontal":
            option = {
                "title":{"text": self.title},
                "legend": legend,
                "tooltip":{"trigger": "axis"},
                "xAxis": {
                    "type": "category",
                    "data": self.x
                },
                "yAxis": {"type": "value"},
                "series": series
            }
        else:
            option = {
                "title":{"text": self.title},
                "legend": legend,
                "tooltip":{"trigger": "axis"},
                "yAxis": {
                    "type": "category",
                    "data": self.x
                },
                "xAxis": {"type": "value"},
                "series": series
            }

        return option  


class Pie:
    def __init__(self, title, data, douhgnut: bool = False, legend: bool = False) -> None:
        self.title = title
        self.data = data
        self.doughnut = douhgnut
        self.legend = legend

    def plot(self):
        radius = ['40%', '70%'] if self.doughnut else '50%'
        option = {
            "title": {
                "text": self.title
            },
            "legend": {"show": self.legend},
            "tooltip": {
                "trigger": 'item'
            },
            "series": [
                {
                    "name": 'Costing',
                    "type": 'pie',
                    "radius": radius,
                    "data": self.data,
                    "emphasis": {
                        "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        }
        return option