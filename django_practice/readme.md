# Django 웹 프로젝트 완전 분석 가이드 📚

> **비전공자를 위한 Django 프로젝트 이해하기**  
---

## 📖 목차
1. [프로젝트 개요](#1-프로젝트-개요)
2. [Django란 무엇인가?](#2-django란-무엇인가)
3. [전체 프로젝트 구조](#3-전체-프로젝트-구조)
4. [각 앱(App)별 상세 분석](#4-각-앱app별-상세-분석)
5. [데이터베이스 구조](#5-데이터베이스-구조)
6. [URL 라우팅 시스템](#6-url-라우팅-시스템)
7. [템플릿과 화면 구성](#7-템플릿과-화면-구성)
8. [프로젝트 실행 방법](#8-프로젝트-실행-방법)
9. [주요 기능 설명](#9-주요-기능-설명)
10. [학습 포인트](#10-학습-포인트)

---

## 1. 프로젝트 개요

### 🎯 이 프로젝트는 무엇인가요?
이것은 **Django**라는 웹 프레임워크를 사용해서 만든 **종합 웹사이트**입니다. 마치 네이버나 다음과 같은 포털 사이트처럼, 여러 가지 기능들이 하나의 웹사이트 안에 들어있어요.

### 🔧 주요 기능들
- **게시판** (질문과 답변)
- **투표 시스템** 
- **회원가입/로그인**
- **간단한 인사말 페이지**
- **JavaScript 연습 페이지**

---

## 2. Django란 무엇인가?

### 🤔 Django를 쉽게 이해하기
Django는 **Python**이라는 프로그래밍 언어로 웹사이트를 만들 수 있게 해주는 **도구 상자**라고 생각하시면 됩니다.

#### 🏠 집짓기와 비교해보면:
- **Django**: 집을 짓기 위한 기본 골조와 도구들
- **앱(App)**: 집안의 각 방 (거실, 침실, 주방 등)
- **모델(Model)**: 가구나 물건들을 정리하는 서랍
- **뷰(View)**: 각 방에서 일어나는 활동들
- **템플릿(Template)**: 각 방의 인테리어와 장식

---

## 3. 전체 프로젝트 구조

```
django_test/mysite/
├── 📁 mysite/           # 프로젝트 설정 (집의 전체 설계도)
├── 📁 board/            # 게시판 앱 (질문답변 게시판)
├── 📁 polls/            # 투표 앱 (설문조사 기능)
├── 📁 common/           # 회원관리 앱 (로그인/회원가입)
├── 📁 skn/              # 간단한 인사말 앱
├── 📁 java_src/         # JavaScript 연습 앱
├── 📁 templates/        # 화면 템플릿들 (웹페이지 디자인)
├── 📁 static/           # 정적 파일들 (CSS, JavaScript, 이미지)
├── 📄 manage.py         # Django 명령어 실행 파일
├── 📄 db.sqlite3        # 데이터베이스 파일 (데이터 저장소)
└── 📄 README.md         # 이 파일!
```

### 🎪 각 폴더의 역할을 놀이공원에 비유하면:
- **mysite/**: 놀이공원 관리사무소 (전체 운영 규칙)
- **board/**: 게시판 놀이기구 (질문과 답변을 올리는 곳)
- **polls/**: 투표 부스 (설문조사 하는 곳)
- **common/**: 입구 게이트 (회원가입, 로그인)
- **templates/**: 각 놀이기구의 디자인
- **static/**: 놀이공원 장식품들 (예쁘게 꾸미는 것들)

---

## 4. 각 앱(App)별 상세 분석

### 🏢 1. mysite 앱 (프로젝트 설정)
**역할**: 전체 프로젝트의 설정과 관리를 담당하는 중앙 관리소

#### 주요 파일들:
- `settings.py`: 프로젝트 전체 설정 파일
  - 데이터베이스 연결 정보
  - 언어 설정 (한국어)
  - 시간대 설정 (서울)
  - 보안 설정
- `urls.py`: 전체 URL 관리 (어떤 주소로 가면 어떤 페이지가 나올지)
- `wsgi.py`: 웹서버와 연결하는 파일

### 📋 2. board 앱 (게시판)
**역할**: 질문과 답변을 올릴 수 있는 게시판 기능

#### 🎯 핵심 기능:
- 질문 목록 보기 (페이지네이션 포함)
- 질문 상세 보기
- 질문 작성/수정/삭제
- 답변 작성/수정/삭제
- 로그인한 사용자만 작성 가능

#### 📁 파일 구조:
```
board/
├── models.py        # 데이터 구조 정의 (질문, 답변 테이블)
├── views/           # 기능 구현 (페이지별 동작)
│   ├── base_views.py     # 기본 기능 (목록, 상세보기)
│   ├── question_views.py # 질문 관련 기능
│   └── answer_views.py   # 답변 관련 기능
├── forms.py         # 입력 양식 (질문/답변 작성 폼)
├── urls.py          # URL 연결 (주소와 기능 매핑)
└── templatetags/    # 템플릿에서 사용하는 추가 기능
```

### 🗳️ 3. polls 앱 (투표 시스템)
**역할**: 설문조사와 투표 기능을 제공

#### 🎯 핵심 기능:
- 투표 질문 목록
- 투표하기
- 투표 결과 보기

#### 📊 데이터 구조:
- **Question**: 투표 질문
- **Choice**: 선택지 (각 질문마다 여러 개)

### 👥 4. common 앱 (회원 관리)
**역할**: 사용자 인증과 관련된 모든 기능

#### 🎯 핵심 기능:
- 회원가입 (이메일 포함)
- 로그인/로그아웃
- 사용자 인증

#### 🔐 보안 특징:
- Django 기본 인증 시스템 사용
- 암호화된 비밀번호 저장
- CSRF 보안 토큰 적용

### 👋 5. skn 앱 (인사말)
**역할**: 간단한 인사말을 보여주는 테스트 앱

#### 📝 학습 포인트:
- Django의 가장 기본적인 구조
- HTML 응답을 직접 반환하는 방법

### 💻 6. java_src 앱 (JavaScript 연습)
**역할**: JavaScript와 관련된 연습 페이지

#### 🎓 학습 목적:
- 프론트엔드 기술 연습
- Django와 JavaScript 연동

---

## 5. 데이터베이스 구조

### 🗄️ 데이터베이스란?
정보를 체계적으로 저장하는 **전자 파일 캐비닛**이라고 생각하세요.

### 📊 현재 프로젝트의 테이블들:

#### 1. **User** 테이블 (Django 기본 제공)
```
👤 사용자 정보
├── username: 사용자ID
├── email: 이메일 주소
├── password: 비밀번호 (암호화됨)
├── first_name: 이름
└── last_name: 성
```

#### 2. **Question** 테이블 (board 앱)
```
❓ 게시판 질문
├── id: 질문 번호 (자동 생성)
├── subject: 제목
├── content: 내용
├── create_date: 작성일시
├── modify_date: 수정일시
└── author: 작성자 (User와 연결)
```

#### 3. **Answer** 테이블 (board 앱)
```
💬 게시판 답변
├── id: 답변 번호 (자동 생성)
├── content: 답변 내용
├── create_date: 작성일시
├── modify_date: 수정일시
├── author: 작성자 (User와 연결)
└── question: 해당 질문 (Question과 연결)
```

#### 4. **Question** 테이블 (polls 앱)
```
🗳️ 투표 질문
├── id: 질문 번호
├── question_text: 질문 내용
└── pub_date: 발행일
```

#### 5. **Choice** 테이블 (polls 앱)
```
☑️ 투표 선택지
├── id: 선택지 번호
├── choice_text: 선택지 내용
├── votes: 득표수
└── question: 해당 질문 (Question과 연결)
```

### 🔗 테이블 간의 관계
- **일대다 관계**: 한 명의 사용자가 여러 질문 작성 가능
- **일대다 관계**: 하나의 질문에 여러 답변 가능
- **일대다 관계**: 하나의 투표 질문에 여러 선택지 가능

---

## 6. URL 라우팅 시스템

### 🗺️ URL이란?
웹사이트의 **주소**입니다. 마치 집 주소처럼 각 페이지마다 고유한 주소가 있어요.

### 🎯 이 프로젝트의 URL 구조:

```
🏠 메인 사이트 (http://localhost:8000/)
├── / ➜ 게시판 메인 페이지
├── /admin/ ➜ 관리자 페이지
├── /skn/ ➜ 인사말 페이지
├── /polls/ ➜ 투표 메인
│   ├── /polls/1/ ➜ 1번 투표 상세
│   ├── /polls/1/vote/ ➜ 1번 투표하기
│   └── /polls/1/results/ ➜ 1번 투표 결과
├── /board/ ➜ 게시판
│   ├── /board/1 ➜ 1번 질문 보기
│   ├── /board/question/create/ ➜ 질문 작성
│   ├── /board/answer/create/1 ➜ 1번 질문에 답변
│   └── ...
├── /common/ ➜ 회원 관리
│   ├── /common/login/ ➜ 로그인
│   ├── /common/logout/ ➜ 로그아웃
│   └── /common/signup/ ➜ 회원가입
└── /javascript/ ➜ JavaScript 연습
```

### 🔄 URL 라우팅 흐름:
1. 사용자가 `/board/`를 입력
2. Django가 `mysite/urls.py`에서 `board/`를 찾음
3. `board/urls.py`로 넘어가서 구체적인 페이지 찾음
4. 해당하는 View 함수 실행
5. 결과를 사용자에게 보여줌

---

## 7. 템플릿과 화면 구성

### 🎨 템플릿이란?
웹페이지의 **디자인 틀**입니다. 워드프로세서의 템플릿과 비슷해요.

### 🏗️ 템플릿 구조:

#### 기본 템플릿 (`base.html`):
```html
<!DOCTYPE html>
<html>
<head>
    <!-- Bootstrap CSS (예쁘게 꾸미는 도구) -->
    <link rel="stylesheet" href="bootstrap.min.css">
    <title>SKN 15기</title>
</head>
<body>
    <!-- 네비게이션 메뉴 -->
    {% include "navi.html" %}
    
    <!-- 각 페이지의 내용이 들어갈 자리 -->
    {% block content %}
    {% endblock %}
    
    <!-- JavaScript 파일들 -->
    <script src="jquery.min.js"></script>
    <script src="bootstrap.min.js"></script>
</body>
</html>
```

#### 주요 템플릿들:
1. **base.html**: 모든 페이지의 기본 틀
2. **navi.html**: 상단 메뉴바
3. **board/question_list.html**: 게시판 목록 페이지
4. **board/question_detail.html**: 게시판 상세 페이지
5. **common/login.html**: 로그인 페이지
6. **common/signup.html**: 회원가입 페이지

### 🎨 디자인 요소:
- **Bootstrap**: CSS 프레임워크 (예쁘게 꾸미는 도구)
- **jQuery**: JavaScript 라이브러리 (동적 기능 추가)
- **한글 인터페이스**: 모든 메뉴와 버튼이 한글로 표시

---

## 8. 프로젝트 실행 방법

### 🚀 서버 시작하기:
```bash
# 1. 프로젝트 폴더로 이동
cd /home/play/workspace/django_test/mysite/

# 2. Django 개발 서버 실행
python manage.py runserver

# 3. 웹브라우저에서 접속
# http://localhost:8000 또는 http://127.0.0.1:8000
```

### 🔧 관리자 계정 만들기:
```bash
# 관리자 계정 생성
python manage.py createsuperuser

# 관리자 페이지 접속: http://localhost:8000/admin/
```

### 📊 데이터베이스 관리:
```bash
# 마이그레이션 파일 생성 (데이터베이스 변경사항 준비)
python manage.py makemigrations

# 마이그레이션 적용 (실제 데이터베이스에 반영)
python manage.py migrate
```

---

## 9. 주요 기능 설명

### 📝 게시판 기능 (Board)

#### 1. **질문 목록 보기**
- 최신 질문부터 표시
- 페이지당 10개씩 표시
- 답변 개수 표시
- 페이지네이션 (이전/다음 버튼)

#### 2. **질문 작성**
- 로그인 필수
- 제목과 내용 입력
- 작성자 자동 저장

#### 3. **답변 작성**
- 로그인 필수
- 질문에 대한 답변
- 여러 개 답변 가능

#### 4. **수정/삭제**
- 본인 작성 글만 가능
- 수정 시 수정일시 자동 업데이트

### 🗳️ 투표 기능 (Polls)

#### 1. **투표 참여**
- 질문 목록에서 선택
- 선택지 중 하나 선택
- 투표 후 결과 확인

#### 2. **결과 보기**
- 각 선택지별 득표수
- 시각적 그래프 (가능시)

### 👤 회원 관리 (Common)

#### 1. **회원가입**
- 사용자명, 이메일, 비밀번호 입력
- 비밀번호 확인
- 가입 후 자동 로그인

#### 2. **로그인/로그아웃**
- Django 기본 인증 시스템
- 로그인 후 메인 페이지로 이동
- 로그아웃 후 메인 페이지로 이동

---

## 10. 학습 포인트

### 🎓 이 프로젝트에서 배울 수 있는 것들:

#### 1. **웹 개발의 기본 구조**
- 클라이언트(브라우저)와 서버의 관계
- HTTP 요청과 응답의 흐름
- MVC 패턴의 이해

#### 2. **Django 프레임워크**
- 프로젝트와 앱의 차이점
- 모델, 뷰, 템플릿의 역할
- URL 라우팅 시스템

#### 3. **데이터베이스**
- 테이블 설계
- 관계형 데이터베이스
- ORM (Object-Relational Mapping)

#### 4. **사용자 인터페이스**
- HTML/CSS의 기초
- Bootstrap 프레임워크
- 반응형 웹 디자인

#### 5. **보안**
- 사용자 인증과 권한
- CSRF 보안
- 비밀번호 암호화

### 📚 더 깊이 학습하려면:

#### 1. **Python 기초**
- 변수, 함수, 클래스
- 조건문, 반복문
- 리스트, 딕셔너리

#### 2. **웹 기초 지식**
- HTML 태그와 구조
- CSS 스타일링
- JavaScript 기본 문법

#### 3. **데이터베이스**
- SQL 기본 쿼리
- 테이블 관계 설계
- 인덱스와 최적화

#### 4. **Django 고급**
- 클래스 기반 뷰
- 미들웨어
- REST API 개발

---

## 🔍 코드 분석 예시

### 간단한 View 함수 이해하기:

```python
# skn/views.py
def Hello(request):
    html = "<h1> 안녕 </h1>"
    return HttpResponse(html)
```

**해석:**
1. `Hello`라는 함수를 정의
2. `request`는 사용자의 요청 정보
3. HTML 코드를 문자열로 작성
4. `HttpResponse`로 HTML을 사용자에게 전송

### 조금 복잡한 View 함수:

```python
# board/views/base_views.py
@login_required(login_url='common:login')
def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'q': page_obj}
    return render(request, 'board/question_list.html', context)
```

**해석:**
1. `@login_required`: 로그인한 사용자만 접근 가능
2. `page = request.GET.get('page', '1')`: URL에서 페이지 번호 가져오기
3. `Question.objects.order_by('-create_date')`: 최신 질문부터 정렬
4. `Paginator`: 페이지 나누기 기능
5. `render`: 템플릿과 데이터를 합쳐서 HTML 생성
