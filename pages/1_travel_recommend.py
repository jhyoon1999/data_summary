import streamlit as st
from st_pages import add_page_title
import pandas as pd

add_page_title(layout = "wide")

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행", "코드"])

#%% 1. 요약

travel_summary = """
<style>
  table {
      width: 100%;
      border-collapse: collapse;
  }
  
  th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: left;
  }
  
  th {
      background-color: #808080;
      color: white;
  }
</style>

<table>
  <tr>
    <th>진행기간</th>
    <td>2023.09-2023.11(3개월)</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">여행자 개인적 특성에 기반한 제주도 관광지 추천웹서비스 개발</td> 
  </tr>
  <tr>
    <th>사용언어/프레임워크</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/python_logo.png" alt="Python Image" width="80" height="50">
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/fastapi_logo.png" alt="FastAPI Image" width="80" height="50">
    </td>
  </tr>
  <tr>
    <th>데이터베이스</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/Mysql_logo.png" alt="MySQL Image" width="80" height="50">
    </td>
  </tr>
</table>
"""

with tab1 :
    subcol1, subcol2 = st.columns([7,3])
    with subcol1 :
        st.subheader("Ⅰ. 프로젝트 개요")
        st.markdown(travel_summary, unsafe_allow_html=True)
    with subcol2 :
        st.text("\n")
        st.text("\n")
        st.write("###### 담당업무(기여도)")
        st.progress(value=100, text = "데이터 수집/가공(100%)")
        st.progress(value=100, text = "분석/시각화(100%)")
        st.progress(value=100, text = "추천시스템 개발(100%)")
        st.progress(value=100, text = "API 개발(100%)")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. 프로젝트 목표")
    st.image("src/travel_recommend/project_purpose.png", use_column_width="auto") ##추후 수정##

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. 프로젝트 프로세스")
    st.image("src/travel_recommend/project_process.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("IV. 결과물")
    with st.expander("01)API Documnet") :
        st.components.v1.html('<iframe src="https://o5as6un2knzd5sl6ldr2gnn3ba0mbgdy.lambda-url.ap-northeast-2.on.aws/docs#/" width="800" height="600"></iframe>', height=600)
    with st.expander("02)최소기능제품") :
        st.components.v1.html('<iframe src="https://jejuai.web.app/#/" width="900" height="600"></iframe>', height=600)

#%%2. 프로젝트 진행
algorithms_info = """
<style>
    table {
        width:100%;
        border-collapse: collapse;
    }

    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #808080;
        color: white;
    }
</style>

<table>
  <tr>
    <th>알고리즘</th>
    <th>라이브러리</th>
    <th>설명</th>
  </tr>
  <tr>
    <td>Hybrid Approach</td>
    <td>LightFM</td>
    <td>Content-based와 Collaborative Filtering의 장점을 결합한 Hybrid 알고리즘</td>
  </tr>
  <tr>
    <td>DeepFM</td>
    <td>LibRecommender</td>
    <td>FM(Factorization Machine)과 딥러닝(DNN)을 결합시킨 알고리즘</td>
  </tr>
  <tr>
    <td>CatBoost</td>
    <td>CatBoost</td>
    <td>Decision-Tree 기반 ensemble method로 범주형 변수에 대한 효율적인 처리를 장점으로 갖는 알고리즘</td>
  </tr>
</table>
"""

@st.cache_data
def call_data_info() :
    travel = pd.read_excel('src/travel_recommend/travel_data.xlsx')
    master = pd.read_excel('src/travel_recommend/travel_master_data.xlsx')
    spot = pd.read_excel('src/travel_recommend/spot_data.xlsx')
    return travel, master, spot

travel, master, spot = call_data_info()

with tab2 :
    #(1). 데이터 수집/가공
    fcol1, fcol2,_ = st.columns([2,8,2])
    with fcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 수집/가공"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with fcol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 : 웹서비스의 기반이 되는 데이터를 수집 후, 개발에 맞게 가공/수정"}</p>\
                    </div>', unsafe_allow_html=True)
            
            
            st.text("1) 데이터 수집 : AI-Hub의 국내 제주 여행로그 데이터")
            # 버튼을 클릭할 때 사용할 상태 변수
            button1_clicked = False
            button2_clicked = False
            button3_clicked = False

            # 버튼을 생성하고 클릭 여부를 확인하는 함수
            def create_button(button_num):
                global button1_clicked, button2_clicked, button3_clicked
                
                if button_num == 1:
                    button1_clicked = st.button("여행 데이터")  # 버튼 1의 이름을 "New Button 1"로 변경
                    if button1_clicked:
                        # 버튼 1이 클릭되면 버튼 2와 버튼 3의 상태를 초기화
                        button2_clicked = False
                        button3_clicked = False
                elif button_num == 2:
                    button2_clicked = st.button("여행객Master")  # 버튼 2의 이름을 "New Button 2"로 변경
                    if button2_clicked:
                        # 버튼 2가 클릭되면 버튼 1과 버튼 3의 상태를 초기화
                        button1_clicked = False
                        button3_clicked = False
                elif button_num == 3:
                    button3_clicked = st.button("방문지데이터")  # 버튼 3의 이름을 "New Button 3"로 변경
                    if button3_clicked:
                        # 버튼 3이 클릭되면 버튼 1과 버튼 2의 상태를 초기화
                        button1_clicked = False
                        button2_clicked = False

            show_data_col1, show_data_col2 = st.columns([2,8])
            
            with show_data_col1 :
                # 버튼을 생성하고 클릭 상태를 확인
                create_button(1)
                create_button(2)
                create_button(3)
            
            with show_data_col2 : 
                # 버튼에 따라 출력할 데이터를 선택하여 출력
                
                
                if button1_clicked:
                    st.dataframe(travel)
                elif button2_clicked:
                    st.dataframe(master)
                elif button3_clicked:
                    st.dataframe(spot)
                else:
                    st.write("")
            
            st.text('')
            st.text('2) 데이터 가공 : 정보가 일부만 존재하는 여행 로그, 검색되지 않는 관광지 탈락/수정')
            st.image('src/travel_recommend/preprocessing.png', use_column_width=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(2). 데이터 분석
    scol1, scol2,_ = st.columns([2,8,2])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 분석"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 : 추천시스템의 성능을 향상시킬 수 있는 파생변수 생성"}</p>\
                    </div>', unsafe_allow_html=True)
            
            st.markdown("""
                        1) 핵심변수 추출 : 여행객의 방문 만족도를 설명하는 핵심변수(Variable Importance) 식별
                            - 사용 알고리즘 : CatBoost
                            - 예측 대상 : 방문 만족도(1점 ~ 5점)
                        """)
            st.image('src/travel_recommend/analysis_1.png', use_column_width=True)
            
            st.markdown("""
                        2) Feature-Engineering : 핵심변수 기반 클러스터링 -> 군집번호를 모델링에서 예측변수로 활용
                            - 군집변수 선택방법 : Elbow Method
                            - 클러스터링 기법 : K-Modes 알고리즘
                        """)
            st.image("src/travel_recommend/analysis_2.png", use_column_width=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(3). 추천시스템 개발
    tcol1, tcol2,_ = st.columns([2,8,2])
    with tcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"추천시스템 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with tcol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 :여행자/관광지 특성을 이용해 여행자의 방문 만족도 점수를 예측하는 머신러닝 모델 개발"}</p>\
                    </div>', unsafe_allow_html=True)
            
            st.text('')
            st.markdown("1) 후보 알고리즘")
            st.markdown(algorithms_info, unsafe_allow_html=True)
            
            st.text('')
            st.markdown('2) 모델링')
            st.image("src/travel_recommend/performance_AI_1.png", use_column_width=True)
            st.image("src/travel_recommend/performance_AI_2.png", use_column_width=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    #(4). API 개발
    focol1, focol2,_ = st.columns([2,8,2])
    with focol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"API 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with focol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 : 추천시스템으로부터 Top 5의 추천 관광지를 산출하고, 결과를 앱에 통신할 수 있는 API 개발 및 배포"}</p>\
                    </div>', unsafe_allow_html=True)
            st.text('')
            st.text('1) API 개발')
            st.image('src/travel_recommend/API_AI.png', use_column_width=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%% 3. 코드
import requests

#1. 데이터 정리
@st.cache_resource
def call_cleaning_user_features_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/1_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%A0%95%EB%A6%AC/01_Data_Cleaning_User_Features.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_cleaning_item_features_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/1_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%A0%95%EB%A6%AC/02_Data_Cleaning_Item_Rating.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_cleaning_dummies_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/1_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%A0%95%EB%A6%AC/03_Data_Cleaning_Dummies.py"
    response = requests.get(github_url)
    code = response.text
    return code

cleaning_user_feautres_code = call_cleaning_user_features_python()
cleaning_item_features_code = call_cleaning_item_features_python()
cleaning_dummies_code = call_cleaning_dummies_python()

#2. 데이터 분석
@st.cache_resource
def call_analysis_clustering_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/2_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%B6%84%EC%84%9D/Clustering_Analysis.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_analysis_importance_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/2_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%B6%84%EC%84%9D/Variable_Importance.py"
    response = requests.get(github_url)
    code = response.text
    return code

analysis_clustering_code = call_analysis_clustering_python()
analysis_importance_code = call_analysis_importance_python()

#3. 추천시스템_머신러닝
@st.cache_resource
def call_ai_catboost_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/3_%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C_%EA%B0%9C%EB%B0%9C/Catboost.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_ai_deepfm_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/3_%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C_%EA%B0%9C%EB%B0%9C/Deep_FM.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_ai_light_fm_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/1_jeju_recommend_web_service/master/3_%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C_%EA%B0%9C%EB%B0%9C/Light_FM.py"
    response = requests.get(github_url)
    code = response.text
    return code

ai_catboost_code = call_ai_catboost_python()
ai_deepfm_code = call_ai_deepfm_python()
ai_light_fm_code = call_ai_light_fm_python()

#4. API 개발
api_code_url = "https://github.com/jhyoon1999/1_jeju_recommend_web_service/tree/master/4_API_%EA%B0%9C%EB%B0%9C"

with tab3 :
    st.write("#### 1. 데이터 정리")
    with st.expander("유저특성 정리 코드") :
        st.code(cleaning_user_feautres_code, language = "python")
    with st.expander("아이템특성 정리 코드") :
        st.code(cleaning_item_features_code, language = "python")
    with st.expander("변수 정리(더미화) 코드") :
        st.code(cleaning_dummies_code, language = "python")
    
    st.write("#### 2. 데이터 분석")
    with st.expander("변수 중요도 분석 코드") :
        st.code(analysis_importance_code, language = "python")
    with st.expander("클러스터링 분석 코드") :
        st.code(analysis_clustering_code, language = "python")
    
    st.write("#### 3. 추천시스템_머신러닝")
    with st.expander("Catboost 모델링 코드") :
        st.code(ai_catboost_code, language = "python")
    with st.expander("DeepFM 모델링 코드") :
        st.code(ai_deepfm_code, language = "python")
    with st.expander("LightFM 모델링 코드") :
        st.code(ai_light_fm_code, language = "python")
    
    st.write("#### 4. API 개발")
    with st.expander("FastAPI 코드") :
        st.link_button("github 바로가기", url = api_code_url)