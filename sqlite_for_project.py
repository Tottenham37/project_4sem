import sqlite3



def input_parametrs():
    connection = sqlite3.connect('rls_project/database4.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Input_parameters')
    parametrs = cursor.fetchone()
    connection.close()
    return parametrs



def parametrs(signal_to_noise_ratio_loss,straight_r,g_prd,g_prm,rls_potential,p,f, s_prd,s_per,r_max, g):
    connection = sqlite3.connect('rls_project/database4.db')
    cursor = connection.cursor()

    cursor.execute('''insert into parameters(сигнал_шум,
    дальность_прямой_видимости, коэффициент_передающей_антенны,
    коэффициент_приемной_антенны, потенциал_РЛС,
    вероятность_обнаружения_цели, вероятность_ложной_тревоги,
    эффективная_площадь_раскрыва_передающей_антенны,
    эффективная_площадь_раскрыва_приемной_антенны,
    максимальная_дальность_обнаружения,
    двусторонняя_диаграмма_направленности_по_мощности) 
    values(?,?,?,?,?,?,?,?,?,?,?)''',
    (signal_to_noise_ratio_loss,straight_r,g_prd,g_prm,rls_potential,p,f, s_prd,s_per,r_max, g))
    connection.commit()
    connection.close()
