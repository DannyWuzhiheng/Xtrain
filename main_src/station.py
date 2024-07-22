import random as rd
import turtle
import pyttsx3
import time
talk = pyttsx3.init()
class T(turtle.Turtle):
    def write(self, arg: object, move: bool = False, align: str = "left", font: tuple[str, int, str] = ...) -> None:
        super().clear()
        super().write(arg, move, align, font)
tur = turtle.Turtle()
tur.pu()
tur.goto(0,150)
tur.pd()
tur.write("校园号列车",font=("宋体",40,"normal"),align='center')
t = T()
t.pencolor("red")
class BusStation:
    def __init__(self, station_name,station_english):
        self.station_name = station_name
        self.station_english = station_english
        self.number_words = {  
        0: 'Zero',  
        1: 'One',  
        2: 'Two',  
        3: 'Three',  
        4: 'Four',  
        5: 'Five',  
        6: 'Six',  
        7: 'Seven',  
        8: 'Eight',  
        9: 'Nine',  
        10: 'Ten',  
        11: 'Eleven',  
        12: 'Twelve',  
        13: 'Thirteen',  
        14: 'Fourteen',  
        15: 'Fifteen',  
        16: 'Sixteen',  
        17: 'Seventeen',  
        18: 'Eighteen',  
        19: 'Nineteen',  
        20: 'Twenty',  
        21: 'Twenty-One',  
        22: 'Twenty-Two',  
        23: 'Twenty-Three',  
        24: 'Twenty-Four',  
        25: 'Twenty-Five'  
    }  
    def Eng(self,n = int):
        return self.number_words[n]
    def announce(self):
        t.write(f"下一站：{self.station_name}.The next stop is {self.station_english}",font=("宋体",15,"normal"),align='center')
        talk.say(f"下一站。。。。。。。。。。：       {self.station_name}.。。。。。。The next stop is............       {self.station_english}")
        talk.runAndWait() 
        talk.stop()
    def arrived(self):
        t.write(f"列车即将进站{self.station_name},the train is arriving at {self.station_english}",font=("宋体",15,"normal"),align='center')
        talk.say(f"列车即将进站    。。。。{self.station_name},。。。。。。。the train is arriving at      。。。。。{self.station_english}")
        talk.runAndWait() 
        talk.stop()        
        a=rd.randint(1,25)
        time.sleep(1.5)
        t.write(f"列车已停靠在{self.station_name},{a}站台,the train has arrived {self.station_english},platform {a}",font=("宋体",15,"normal"),align='center')
        talk.say(f"列车已停靠在     。。{self.station_name},{a}站台,。。。the train has arrived      。。{self.station_english},platform {self.Eng(a)}")
        talk.runAndWait() 
        talk.stop()      
class BusRoute:
    def __init__(self, route_name, stations = list,english_station = str,chinese_station =str):
        self.route_name = route_name
        self.stations = stations
        self.english_station = english_station
        self.current_station_index = 0
        self.chinese_station = chinese_station
    def next_station(self):
        if self.current_station_index < len(self.stations):
            current_station = self.stations[self.current_station_index]
            self.current_station_index += 1
            current_station.announce()
            time.sleep(4.5)
            current_station.arrived()
            time.sleep(1)
        else:
            t.write(f"已经到达终点站:{self.chinese_station}，请下车，We arrived the last stop {self.english_station}",font=("宋体",15,"normal"),align='center')
            talk.say(f"已经到达终点站:       。。。。。{self.chinese_station}，请下车。。。。。We arrived the last stop          。。。。{self.english_station}")
            talk.runAndWait() 
            talk.stop() 
    def start_route(self):
        t.write(f"欢迎乘坐由罗源县实验小学客运段直骋的{self.route_name}动车组列车，本次列车终点站：{self.chinese_station}",font=("宋体",15,"normal"),align='center')
        self.ap=self.route_name.replace('X','校')
        talk.say(f"欢迎乘坐由罗源县实验小学客运段直骋的  。。。。{self.ap}  动车组列车，本次列车终点站：      。。。{self.chinese_station}")
        talk.runAndWait() 
        talk.stop() 
        self.next_station()
if __name__ == "__main__":
    station1 = BusStation("6楼","sixth floor")
    station2 = BusStation("操场","playground")
    station3 = BusStation("校门口","the gate")
    route_name = turtle.textinput("输入您乘坐的列车车号：","")
    if "X" in route_name:

        try:
            money = int(turtle.textinput("输入您购票的价格：","标准价格 = 10元"))
        except:
            t.write("价格格式错误",font=("宋体",25,"normal"),align='center')
        if money >= 10:

            route1 = BusRoute(route_name, [station1, station2, station3],"the gate","校门口")
            route1.start_route()
            route1.next_station()
            route1.next_station()
        else:
            t.write("价格太低，无法乘车")
            exit()
    else:
        t.write("车号错误")
        exit()