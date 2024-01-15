# 자동화 플랜

###  테스트 프레임워크 선정 기준

+ Flutter 로 개발된 Application 의 경우 Flutter Integration Test 를 활용 하겠지만, (Key 작성 과 Widget 에 Key 를 넣어줘야 하는 과정이 존재하지만 Appium 에 비해 강력하고 변하지 않는 Selector 그러나 Flutter 로 개발된 Application 에서만 사용 가능함)
  
+ Application 을 검증해야 하는 과제 이므로
Mobile Automation Test 에 널리 활용되고 있으며 크로스 플랫폼 (IOS/AOS) 사용 가능하고 또한 언어 및 프레임워크의 유연성을 가진 (Java,Python,JavaScript,Ruby) 
하이브리드,네이티브 모두 활용가능한 Appium 을 활용.


### GUI로 자동화 가능한 영역

+ 해외여행보험>가입 시나리오, 가입 이후 의 모든 영역 (인증번호 영역 및 결제 관련 기능 또한 가능 하다고 판단.)
"CLUe" 의 모든 UI (Click,Swipe,Scrolling,SendKey 등의 UI와 상호작용이 가능한 영역)
+ 본 Test에 필요한 최소한의 함수들은 Uitl 파일에 작성 하였습니다. 자세한 사항은 파일 안의 내용 확인 부탁드립니다.

### API 자동화 가능한 영역

+ 
### 자동화 구현 중 발생 할 수 있는 문제점 및 해결 방안

+ 추가 된 UI 로 인한 Selector 변경
  + Xpath 등의 변경이 쉬운 Selector 로 Code 를 구성한 경우 UI 가 변경될 경우 이전 Code 를 찾아가 새로운 Xpath 로 변경해야하는 번거로움이 있음
    + 하여 개발자와의 협업을 통해 ClassName 으로 UI 를 정의 하는것이 이상적인 방향

+ 동기화 문제 (타이밍 이슈)
  + UI 간 상호작용 중 네트워크 및 테스트 디바이스 성능 이슈로 인하여 다음 코드를 실행하지 못하는 Test Fail 이 자주 발샐된다, 이를 방지하기 위하여 sleep time 을 적절히 사용해야 한다
+ Test Code 의 복잡성
  + Test code 가 과다하게 복잡해지는 경우 lagacy code 를 야기한다, 하여 항상 타 QE 들과 Review 과정을 진행하고, Test code 는 간결하고 명확하게 작성할 수 있도록 해야한다. (함수명,클래스명,폴더명 등등)  

### 테스트 리포트 구성 방안

+ Intellij Test Report 제공 (HTML 형태 간결한 UI)
+ Reporting Frameword 활용 (Allure,ReportNG)
+ Slcak 을 통한 Report 자동 전송 (Test 종료 시 설정된 Email 로 전송하는 방법)
+ Jenkins/Firebase Testlab 의 TestReport 활용
