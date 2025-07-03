import tableauserverclient as TSC

# Tableau Server 정보 설정
TABLEAU_SERVER_URL = 'https://bi.dfocus.net/'  # Tableau Server 또는 Tableau Cloud의 URL
USERNAME = 'jhlee'  # Tableau 사용자 이름
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # <======= Tableau 비밀번호
SITE_ID = '999_'  # 사이트 ID (기본 사이트의 경우 빈 문자열)

# Tableau 인증 및 서버 객체 생성
tableau_auth = TSC.TableauAuth(USERNAME, PASSWORD, site_id=SITE_ID)
server = TSC.Server(TABLEAU_SERVER_URL, use_server_version=True)

# 데이터 소스 목록 조회
with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("데이터 소스 목록:")
    for datasource in all_datasources:
        print(f"이름: {datasource.name}, LUID: {datasource.id}")
