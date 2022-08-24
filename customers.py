from datetime import datetime
customers = [
    {
        "customer_email": "maitrongthuan0208@gmail.com",
        "customer_name": "Mai Trọng Thuần",
        'ma_khach_hang': 'PD22010146843',
        'contract_id': '8403',
        'ticket_id': '15313'
    },
    {
        "customer_email": "ginginyb@gmail.com",
        "customer_name": "Phạm Lê Khánh Huyền",
        'ma_khach_hang': 'PD22010146844',
        'contract_id': '8404',
        'ticket_id': '15314'
    },
    # {
    #     "customer_email": "hungevnhanoi@gmail.com",
    #     "customer_name": "Nguyễn Việt Hùng",
    #     'ma_khach_hang': 'PD22010146841',
    #     'contract_id': '8401',
    #     'ticket_id': '15311'
    # },
    # {
    #     "customer_email": "oanhlkb9@gmail.com",
    #     "customer_name": "Chị Oanh",
    #     'ma_khach_hang': 'PD22010146842',
    #     'contract_id': '8402',
    #     'ticket_id': '15312'
    # },
]

baseUrl = 'http://125.212.225.71:8081'

NOW = datetime.now().strftime("%d/%m/%Y")
