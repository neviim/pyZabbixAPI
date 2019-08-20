# utilizando anaconta3 python3.7

    # Instalar

        # Dependencias

            >> conda install py-zabbix


        # criar arquivo: conf/config.json
            {
                "zabbix":{
                    "host": "http://zabbix.server/",
                    "user": "id_uruario",
                    "pwd":  "senha"
                },
                "other":{
                    "user_anonymous": false
                }
            }

        # uso:
            $ python src/pyzabbixAcesso.py



# Testando ZabbixAPI em ipython

$ ipython
>>>
>>> import ZabbixAPI 
>>>
>>> z = ZabbixAPI('https://zabbix.server', user='Admin', password='zabbix')
>>> z.host.get(status=1) // Get todos hosts desativados

{ 'hostid': '10433',
  'proxy_hostid': '0',
  'host': 'ins30750',
  'status': '0',
  'disable_until': '1566311828',
  'error': 'Get value from agent failed: cannot connect to [[ins30750.dominio.com]:10050]: [4] Interrupted system call',
  'available': '2',
  'errors_from': '1566304298',
  'lastaccess': '0',
  'ipmi_authtype': '-1',
  'ipmi_privilege': '2',
  'ipmi_username': '',
  'ipmi_password': '',
  'ipmi_disable_until': '0',
  'ipmi_available': '0',
  'snmp_disable_until': '0',
  'snmp_available': '0',
  'maintenanceid': '0',
  'maintenance_status': '0',
  'maintenance_type': '0',
  'maintenance_from': '0',
  'ipmi_errors_from': '0',
  'snmp_errors_from': '0',
  'ipmi_error': '',
  'snmp_error': '',
  'jmx_disable_until': '0',
  'jmx_available': '0',
  'jmx_errors_from': '0',
  'jmx_error': '',
  'name': 'ins30750',
  'flags': '0',
  'templateid': '0',
  'description': '',
  'tls_connect': '1',
  'tls_accept': '1',
  'tls_issuer': '',
  'tls_subject': '',
  'tls_psk_identity': '',
  'tls_psk': '',
  'proxy_address': '',
  'auto_compress': '1'}






>>> z.host.get(status=0) // Get todos hosts ativados

{ 'hostid': '10453',
  'proxy_hostid': '0',
  'host': 'Zabbix server',
  'status': '0',
  'disable_until': '0',
  'error': '',
  'available': '1',
  'errors_from': '0',
  'lastaccess': '0',
  'ipmi_authtype': '-1',
  'ipmi_privilege': '2',
  'ipmi_username': '',
  'ipmi_password': '',
  'ipmi_disable_until': '0',
  'ipmi_available': '0',
  'snmp_disable_until': '0',
  'snmp_available': '0',
  'maintenanceid': '0',
  'maintenance_status': '0',
  'maintenance_type': '0',
  'maintenance_from': '0',
  'ipmi_errors_from': '0',
  'snmp_errors_from': '0',
  'ipmi_error': '',
  'snmp_error': '',
  'jmx_disable_until': '0',
  'jmx_available': '0',
  'jmx_errors_from': '0',
  'jmx_error': '',
  'name': 'Zabbix server',
  'flags': '0',
  'templateid': '0',
  'description': '',
  'tls_connect': '1',
  'tls_accept': '1',
  'tls_issuer': '',
  'tls_subject': '',
  'tls_psk_identity': '',
  'tls_psk': '',
  'proxy_address': '',
  'auto_compress': '1'}


# Send...
>>> from pyzabbix import ZabbixMetric, ZabbixSender
>>>
>>> metrics = []
>>> m = ZabbixMetric('localhost', 'cpu[usage]', 20)
>>> metrics.append(m)
>>> zbx = ZabbixSender('127.0.0.1')
>>> zbx.send(metrics)
