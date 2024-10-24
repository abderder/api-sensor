from calendar import month
from datetime import date, timedelta
import numpy as np
import sys



class VisitSensor:
    def __init__(
        self,
        avg_visit: int,
        std_visit: int,
        perc_break: float = 0.015,
        perc_malfunction: float = 0.035,
    )-> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_break = perc_break
        self.perc_malfunction = perc_malfunction
    def simulate_visit(self, business_date: date) -> int:
        np.random.seed(seed=business_date.toordinal())
        week_day = business_date.weekday()
        visit = np.random.normal(self.avg_visit,self.std_visit)
        if week_day == 2:
            visit *= 1.10
        if week_day == 4:
            visit *= 1.25
        if week_day == 5:
            visit *= 1.35
        if week_day == 6:
            visit = -1
        return np.floor(visit)
    def get_visit_count(self, business_date: date) -> int :
        np.random.seed(seed=business_date.toordinal())
        proba_malfunction = np.random.random()

        if proba_malfunction < self.perc_break:
            print("break")
            return 0
        visit = self.simulate_visit(business_date)
        if proba_malfunction < self.perc_malfunction:
            print("malfunction")
            visit = np.floor(visit*0.2)
        return visit
# capteur = VisitSensor(1800,150)
# init_date = date(2022,1,1)
# c=0
# while init_date < date(2024,1,1):
#     init_date += timedelta(days=1)
#     vis = capteur.get_visit_count(init_date)
#     print(vis)
#     if vis <1000:
#         c+=1
# print("***********",c)
#
# if (len(sys.argv) > 1):
#     year, month, day = [int(v)-1 for v in sys.argv[1].split("-")]
# else:
#     year, month, day = 2023, 10, 25
# q_date = date(year, month, day)
# capteur = VisitSensor(1500,150)
# print(f"date : {q_date} -> {capteur.simulate_visit(q_date)}")
# print(f"date : {q_date} -> {capteur.get_visit_count(q_date)}")
