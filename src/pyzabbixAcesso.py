from pyzabbix import ZabbixMetric, ZabbixSender
from pyzabbix.api import ZabbixAPI

import os
import json


# --- config acesso
def config():
    
    configfile_name = "conf/config.json"

    # Verifique se já existe um arquivo de configuração
    if not os.path.isfile(configfile_name):
        print("Arquivo config.json não encontrado, modelo em README.")
        exit()
    else:
        with open('conf/config.json') as json_data_file:
            data = json.load(json_data_file)

        # print(data['zabbix']['host'])
        return data



# --- Hostname
def hostname(zapi):
    
    # Get todos host monitorados
    result1 = zapi.host.get(monitored_hosts=1, output='extend')

    # Get todos host desativados
    result2 = zapi.do_request('host.get',
                            {
                                'filter': {'status': 1},
                                'output': 'extend'
                            })

    # Filtra resultado
    hostnames1 = [host['host'] for host in result1]
    hostnames2 = [host['host'] for host in result2['result']]

    # Logout do Zabbix
    zapi.user.logout()

    return hostnames1, hostnames2


# --- sendMetrica
def sendMetrica():
    # Send metrics to zabbix trapper
    packet = [
        ZabbixMetric('hostname1', 'test[cpu_usage]', 2),
        ZabbixMetric('hostname1', 'test[system_status]', "OK"),
        ZabbixMetric('hostname1', 'test[disk_io]', '0.1'),
        ZabbixMetric('hostname1', 'test[cpu_usage]', 20, 1411598020),
    ]

    result = ZabbixSender(use_config=True).send(packet)

    return result


# --- main
def main():
    # config acesso 
    data = config()  

    # Cria ZabbixAPI class instance
    zabiixAPI = ZabbixAPI(url=data['zabbix']['host'], user=data['zabbix']['user'], password=data['zabbix']['pwd'])

    host1, host2 = hostname(zabiixAPI)
 
    print(host1)
    print("\n")
    print(host2)
 


# --- inicio
if __name__ == "__main__":
    main()    
