
import numpy as np

from fake_data_app.sensor import VisitSensor
from datetime import date


class StoreSensor:
    def __init__(
            self,
            name: str,
            avg_visit: int,
            std_visit: int,
            perc_malfunction: float=0,
            perc_break: float=0,
    ) -> None:
        self.name = name
        self.sensors = list()

        seed = np.sum(list(self.name.encode('ascii')))

        np.random.seed(seed)
        traffic_percentage = [0.48, 0.30, 0.05, 0.03, 0.01, 0.02, 0.10, 0.01]
        np.random.shuffle(traffic_percentage)
        for i in range(8):
            sensor = VisitSensor(
                traffic_percentage[i]*avg_visit,
                traffic_percentage[i]*std_visit,
                perc_malfunction,
                perc_break,
            )
            self.sensors.append(sensor)
    def get_sensor_traffic(self, sensor_id: int ,business_date: date)->int:
        return self.sensors[sensor_id].get_visit_count(business_date)
    def get_all_traffic(self, business_date: date):
        visit = 0
        for i in range(len(self.sensors)):
            visit += self.sensors[i].get_visit_count(business_date)
        return visit

# if __name__ == "__main__":
#     magasin = StoreSensor('JAUDE',1500,200)
#     print(magasin.name)
#     year, month, day = 2024, 8, 24
#     q_date = date(year, month, day)
#     s = 0
#     somme = sum([magasin.get_sensor_traffic(i,q_date) for i in range(0,8)])
#     print(somme)
#     print(magasin.get_all_traffic(q_date))

# lille_store = StoreSensor("Lille",1200,300)
# visits = lille_store.get_all_traffic(date(2023,9,13))
# print(visits)