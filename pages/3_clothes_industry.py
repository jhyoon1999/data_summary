import streamlit as st
from st_pages import add_page_title


add_page_title(layout = "wide")
# 사이드바에 추가할 이미지 파일의 경로
image_path = 'src/introduction/company_logo.png'

# 사이드바에 이미지 추가
st.sidebar.image(image_path, use_column_width=True)

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행","코드"])

#%% 1. 요약

JWI_summary = """
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
    <td>2022.06-2022.12(6개월)</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">COVID-19 사태 전/후 국내 의류산업 변동에 대한 인사이트 발견</td> 
  </tr>
  <tr>
    <th>사용언어</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/R_logo.jpg" alt="R Image" width="80" height="50">
    </td>
  </tr>
  <tr>
    <th>앱 개발</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/shiny_logo.png" alt="Shiny Image" width="80" height="50">
    </td>
</table>
"""


with tab1 :
    subcol1, subcol2 = st.columns([7,3])
    with subcol1 :
        st.subheader("Ⅰ. 프로젝트 개요")
        st.markdown(JWI_summary, unsafe_allow_html=True)
    with subcol2 :
        st.text("\n")
        st.text("\n")
        st.write("###### 담당업무(기여도)")
        st.progress(value=30, text = "데이터 수집/가공(30%)")
        st.progress(value=80, text = "분석 앱 개발(90%)")
        st.progress(value=70, text = "데이터 분석(80%)")
        st.progress(value=50, text = "인사이트 보고서(50%)")

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)

    st.subheader("Ⅱ. 프로젝트 목표")
    st.image("src/JWi/project_purpose.png", use_column_width="auto") ##추후 수정##

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. 프로젝트 프로세스")
    st.image("src/JWi/project_process.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("IV. 결과물")
    with st.expander("01)분석 앱") :
        st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/JWi/app_vis.png", use_column_width="auto")
    with st.expander("02)인사이트 보고서") :
        st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/JWi/insight_img.png", use_column_width="auto")

#%%2. 프로젝트 진행
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
                        <p style="font-weight:bold;">{"목적 :1) 데이터 수집, 2) 기업 건전성 지표 생성"}</p>\
                    </div>', unsafe_allow_html=True)
            st.text('')
            st.markdown("""
                        1) 데이터 수집 : 국내 의류산업 기업 정보 데이터
                            - 출처 : 2016 ~ 2022년도 NICE D&B 기업 정보 데이터
                        """)
            st.image('src/JWi/missing_value.png', use_column_width="auto")
            st.text('')
            st.markdown("""
                        2) 기업 건전성 지표 생성
                            - 참고자료 : 2019년 기업 경영분석 보고서(한국은행 발행)
                        """)
            st.image('src/JWi/variable_img.png', use_column_width="auto")
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(2). 분석 앱 개발
    scol1, scol2,_ = st.columns([2,8,2])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"분석 앱 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 : 데이터 분석 앱 개발"}</p>\
                    </div>', unsafe_allow_html=True)
            st.text('')
            st.markdown("""
            1) 분석 앱 개발 : 클라이언트가 실시간으로 각 시나리오 하에서 통계 검증/분석/시각화가 가능한 분석 앱 개발
                - 프레임워크 : RShiny
                - 배포 : shinyapps.io
            """)
            st.image('src/JWi/result_app.png', use_column_width="auto")
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(3). 데이터 분석
    tcol1, tcol2,_ = st.columns([2,8,2])
    with tcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 분석"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with tcol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 :1) 핵심변수 식별, 2) 인사이트 도출"}</p>\
                    </div>', unsafe_allow_html=True)
            st.text('')
            st.markdown("""
                        1) 핵심변수 식별 
                            - 방법 : 기업 건전성 지표를 COVID-19 사태 전/후로 분류(classification)하는 모델링을 통해 주요 변수 식별 
                        """)
            st.image('src/JWi/analysis_1.png', use_column_width="auto")
            st.image('src/JWi/analysis_2.png', use_column_width="auto")
            st.text('')
            st.markdown("""
                        2) 인사이트 도출
                            - 연도별 기업 정보가 신고된 기업 수 차이에 주목 -> 데스크 리서치 실시
                            - 결과 : 신고되지 않은 기업 중 약 70%가 휴/폐업 또는 업종 변경
                        """)
            st.image('src/JWi/insight.png', use_column_width="auto")
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(4). 보고서 작성
    tcol1, tcol2,_ = st.columns([2,8,2])
    with tcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"보고서 작성"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with tcol2 :
            st.text('')
            st.markdown(f'<div style="position:relative; text-align:left;">\
                        <p style="font-weight:bold;">{"목적 : 데이터 분석을 통해 추출한 인사이트 기반 보고서 작성"}</p>\
                    </div>', unsafe_allow_html=True)
            st.text('')
            st.image('src/JWi/insight_img.png', use_column_width="auto")
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%%3. 코드
import requests

@st.cache_resource
def call_shiny_app_r() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/3_Analysis_of_the_domestic_clothing_industry/master/%EB%B6%84%EC%84%9D%20%EC%95%B1/app.R"
    response = requests.get(github_url)
    code = response.text
    return code

shiny_app_code = call_shiny_app_r()

with tab3 :
    with st.expander("분석 앱 개발 코드") :
        st.code(shiny_app_code, language = "r")