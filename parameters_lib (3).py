import math

class Parameters:
    def __init__(self, h_antenna, h_air_obj, epr_target, e_prd, e_prm, r, k, v_p, s, sigma, f_per, f_pr, l_per_b, l_per_e, l_pr_b, l_pr_e, n, k_ch, t0, w_a):
        self.t0 = t0 #период повторения импульсов
        self.w_a = w_a #w_a - угловая скорость вращения антенны(рад/с)
        self.k_ch = k_ch #k_ch - коэффициент когерентности
        self.l_per_b = l_per_b #l_per_b, l_per_e - апертура передающей антенны РЛС в гор.и верт.пл-тях
        self.l_per_e = l_per_e
        self.l_pr_b = l_pr_b #l_pr_b, l_pr_e - апертура приемной антенны РЛС в гор.и верт.пл-тях
        self.l_pr_e = l_pr_e
        self.n = n #n- коэффициент использования геометрической площади антенны
        self.f_per = f_per #f_per, f_pr - значания нормированных диаграмм направленности
        self.f_pr = f_pr
        self.v_p = v_p #пороговый уровень
        self.s = s #средний уровень эхо-сигнала цели
        self.sigma = sigma #средний уровень шума
        self.k = k #удельный коэффициент поглощения радиоволн в нижних слоях атмосферы
        self.r = r #расстояние до цели
        self.h_antenna = h_antenna  #высота фазового центра антенны
        self.h_air_obj = h_air_obj  #высота наблюдаемого воздушного объекта
        self.epr_target = epr_target    #ЭПР цели
        self.e_prd = e_prd #угломестное направление передающего луча
        self.e_prm = e_prm #для приемной антенны
        self.p_izl = 1 * 10 ** 5  #импульсная мощность излучаемого сигнала
        self.t_i = 1 * 10 ** -4  #длительность импульса
        self.dna_width = 10000  #ширина ДНА
        self.g_prd = 40  #коэффициенты усиления передающей антенны
        self.g_prm = 40  #коэффициент усиления приемной антенны
        self.g_prd_earth = None #с учетом влияния Земли
        self.g_prm_earth = None #с учетом влияния Земли
        self.etha_prd = None #поправочные коэффициенты
        self.etha_prm = None
        self.etha_total = None
        self.g = None #двусторонняя диаграмма направленности по мощности
        self.wave_length = 0.035  #длина волны
        self.noise_factor = 5    #шум-фактор приемного устройства
        self.prd_loss = 1.5
        self.prm_loss = 1.5
        self.proc_loss = 1
        self.atm_loss = None
        self.prob_false_warn = 1 * 10 ** -6  #вероятность ложной тревоги
        self.k_bolzman = 1.38 * 10**-23  #постоянная Больцмана
        self.standart_temp = 290  #стандартная температура
        self.signal_to_noise_ratio = None   #сигнал-шум без потерь
        self.total_loss = None    #суммарный кэф потерь
        self.signal_to_noise_ratio_loss = None  #сигнал-шум с потерями
        self.straight_r = None #дальность прямой видимости
        self.r_earth = 6371210
        self.e = None #угол места цели
        self.p = None #вероятность обнаружения цели
        self.f = None #вероятность ложной тревоги
        self.rls_potential = None
        self.s_per = None #эффективная площадь раскрыва передающей антенны
        self.s_prd = None #эффективная площадь раскрыва приемной антенны
        self.max_r = None #максимальная дальность обнаружения
        self.p0 = None #значение фиксированного порога обнаружения
        self.m = None #пачка отраженных импульсов



    def calc_cnr(self):
        self.signal_to_noise_ratio = ((self.p_izl * self.g_prd * self.g_prm * self.wave_length**2 * self.epr_target)/
                                 ((4*math.pi)**3 * self.r**4 * self.noise_factor * self.k_bolzman * self.standart_temp))


    def calc_cnr_loss(self): #вычисление отношения сигнал-шум
        if self.total_loss is None or self.signal_to_noise_ratio is None:
            raise ValueError("Не вычислен суммарный коэффициент потерь или сигнал-шум без потерь")
        self.signal_to_noise_ratio_loss = self.signal_to_noise_ratio * self.total_loss


    def calc_total_loss(self): #вычисление суммарного коэффициента потерь
        if self.atm_loss is None:
            raise ValueError("Не вычислен коэффициент потерь из-за атмосферы")
        self.total_loss = self.prd_loss * self.prm_loss * self.proc_loss * self.atm_loss



    def calc_r(self, signal_to_noise_ratio): #signal_to_noise_ratio - данный нам сигнал-шум
        if self.total_loss is None:
            raise ValueError("Не вычислен суммарный коэффициент потерь")
        self.r = (((self.p_izl * self.g_prd * self.g_prm * self.wave_length**2 * self.epr_target * self.total_loss)/
             ((math.pi*4)**3 * signal_to_noise_ratio * self.k_bolzman * self.standart_temp)))**0.25



    def calc_atm_loss(self):
        if self.e is None:
            raise ValueError("Не вычислен угол места цели")
        h_a = 7500
        r_max = (self.r_earth**2 * (math.sin(self.e))**2 + h_a*(h_a + 2*self.r_earth))**0.5 - self.r_earth*math.sin(self.e)
        r_atm = min(self.r, r_max)
        self.atm_loss = 10**(-2*self.k*r_atm)



    def calc_straight_r(self): #вычисление дальности прямой видимости
        self.straight_r = 4.12*(self.h_antenna**0.5 + self.h_air_obj**0.5)



    def calc_e(self): #вычисление угла места цели
        self.e = (math.acos(((self.r_earth+self.h_air_obj)**2 - (self.r_earth+self.h_antenna)**2 - self.r**2)/
                  (-2*self.r*(self.r_earth+self.h_antenna))) - math.pi/2)


    def A(self, e):
        x = (1.392*e)/(math.radians(self.dna_width)/2)
        a = math.sin(x)/x
        return a

    #дальше идут 3 фукнции, которые вычисляют кэфы усиления антенны с учетом влияния Земли с их поправочными кэфами


    def calc_g_prd_earth(self, k):#k-свободная переменная
        l_a = -4/3*self.r_earth*k + ((4/3*self.r_earth*k)**2 + 2*4/3*self.r_earth*self.h_antenna + self.h_antenna**2)**0.5
        l_obj = -4/3*self.r_earth*k + ((4/3*self.r_earth*k)**2 + 2*4/3*self.r_earth*self.h_air_obj + self.h_air_obj**2)**0.5
        r = ((l_a+l_obj)**2 - 4*l_a*l_obj*(k**2))**0.5
        d_phi = math.pi + (2*math.pi*(l_a+l_obj-r))/self.wave_length
        e_obj = (math.acos(((4/3*self.r_earth + self.h_air_obj) ** 2 - (4/3*self.r_earth + self.h_antenna) ** 2 - r ** 2) /
                       (-2 * r * (4/3*self.r_earth + self.h_antenna))) - math.pi / 2)
        delta = math.acos((l_obj**2-l_a**2-r**2)/(-2*l_a*r))
        e_earth = e_obj - delta
        self.g_prd_earth = ((self.A(e_obj-self.e_prd)+1*self.A(e_earth-self.e_prd)*math.cos(d_phi))**2 +
                            (1**2)*(self.A(e_earth-self.e_prd)**2 * (math.sin(d_phi))**2))
        self.etha_prd = self.g_prd_earth/(self.A(e_obj-self.e_prd)**2)



    def calc_g_prm_earth(self, k): #k - сводобная переменнная
        l_a = -4/3*self.r_earth*k + ((4/3*self.r_earth*k)**2 + 2*4/3*self.r_earth*self.h_antenna + self.h_antenna**2)**0.5
        l_obj = -4/3*self.r_earth*k + ((4/3*self.r_earth*k)**2 + 2*4/3*self.r_earth*self.h_air_obj + self.h_air_obj**2)**0.5
        r = ((l_a+l_obj)**2 - 4*l_a*l_obj*(k**2))**0.5
        d_phi = math.pi + (2*math.pi*(l_a+l_obj-r))/self.wave_length
        e_obj = (math.acos(((4/3*self.r_earth + self.h_air_obj) ** 2 - (4/3*self.r_earth + self.h_antenna) ** 2 - r ** 2) /
                       (-2 * r * (4/3*self.r_earth + self.h_antenna))) - math.pi / 2)
        delta = math.acos((l_obj**2-l_a**2-r**2)/(-2*l_a*r))
        e_earth = e_obj - delta
        self.g_prm_earth = ((self.A(e_obj-self.e_prm)+1*self.A(e_earth-self.e_prm)*math.cos(d_phi))**2 +
                            (1**2)*(self.A(e_earth-self.e_prm)**2 * (math.sin(d_phi))**2))
        self.etha_prm = self.g_prm_earth / (self.A(e_obj - self.e_prm) ** 2)



    def calc_g(self):
        if self.g_prm_earth is None or self.g_prd_earth is None:
            raise ValueError("Не вычислены кэфы усиления с учетом влияния Земли")
        self.g = self.g_prd_earth*self.g_prm_earth
        self.etha_total = self.etha_prm * self.etha_prd

    #функции для расчета вероятностей

    def calc_p_f(self): #если задана вероятность ложных тревог
        if self.calc_cnr_loss is None or self.f is None:
            raise ValueError("Не рассчитано отношение сигнал шум с учетом погрешностей или вероятность ложной тревоги")
        self.p = self.f**(1/(1+self.signal_to_noise_ratio_loss))


    def calc_p_vp(self):
        self.p = math.e**((-self.v_p)/(1+self.s/(self.sigma**2)))



    def calc_f(self):
        self.f = 10**-6

    #расчет потенциала РЛС
    def calc_rls_potential(self):
        if self.total_loss is None:
            raise ValueError("Не вычислен потенциал РЛС: недостаточно данных")

        self.rls_potential = ((self.p_izl*self.g_prm*self.g_prd*(self.wave_length**2)*self.total_loss*self.f_per*self.f_pr)/
                              ((4*math.pi)**3 * self.k_bolzman*293*self.dna_width*self.noise_factor))


    #расчет эффективной площади раскрыва передающей антенны
    def calc_s_per(self):
        self.s_per = self.l_per_b * self.l_per_e * self.n


    #расчет эффективной площади раскрыва приемной антенны
    def calc_s_prd(self):
        self.s_prd = self.l_pr_b * self.l_pr_e * self.n



    #расчет максимальной дальности обнаружения
    def calc_max_r(self):
        if self.p0 is None or self.rls_potential is None:
            raise ValueError("Не вычислено значение фиксированного порога обнаружения или потенциал РЛС")
        self.r_max = (self.rls_potential * self.epr_target / self.p0)**(0.25)

    #расчет фиксированного порога обнаружения
    def calc_p0(self):
        if self.m is None:
            raise ValueError("Не вычислена пачка отраженных импульсов")
        if self.p is None or self.f is None:
            raise ValueError("Не вычислена вероятность ложной тревоги или обнаружения цели")
        self.p0 = math.sqrt((1/(self.m**self.k_ch)) * ((math.log10(self.f))/math.log10(self.p) - 1))


    #расчет количества импульсов в пачке
    def calc_m(self):
        self.m = 1 + math.trunc(self.dna_width*0.5*self.t0/self.w_a)



#use











