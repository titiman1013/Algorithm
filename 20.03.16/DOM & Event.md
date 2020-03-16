# DOM
- 문서의 구조화된 표현을 제공, DOM 구조에 접근 할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 돕고, 구조화된 노드와 오브젝트로 문서를 표현
- 주요 객체
    1. window: DOM 문서를 표현하는 창, 가장 최상위 객체
        - window 객체는 전역 객체
        - 다양한 함수, 이름공간, 객체 등이 포함
        - 사용하는 모든 변수의 이름공간
    2. document: 페이지 콘텐츠의 진입점 역할을 하며, <body> 등 다른 요소들을 포함
    3. mavigator, location, history, screen

### DOM 접근 (하이라이팅된 것을 사용하는것이 좋음)
- 단일 Node
    - __document.querySelector(selector)__ 
    - document.getElementByID(id) --> 하나의 단일 node를 리턴, 나머지는 유사 배열 형태로 리턴
- HTMLCollection(live)
    - document.getElementsByTagName(class)
    - document.getElementsByClassName(class)
- NodeList(non-live)
    - __document.querySelectorAll(selector)__

- HTML Collection은 모두 live collection이며, 활용시 주의를 요한다.
- NodeList는 경우에 따라 live collection일 수 있다.

# Event
- 브라우저에서 특정한 이벤트가 발생하면 이에 대한 이후 행위를 정의할 수 있다.
- 이벤트를 정의하는 경우, 인라인으로도 작성 가능하나 분리하여 작성할 수도 있다.

1. addEventListener
    - EventTarget.addEventListener(type, listener, [, useCapture]);
        - type: 이벤트 유형
        - listener: 이벤트가 발생했을 때 실행할 콜백 함수(핸들러)
        - useCapture: 기본 값(false), 상위 노드로 전파(버블링), 만약 true인 경우 하위 노드로 전파(캡처링)
2. 이벤트 전파
    - Event는 해당 요소에서 전파되며, 캡처링과 버블링으로 구분된다.
    - 항상 캡처링부터 시작하여 버블링으로 종료되며, addEventListener 메소드의 useCapture를 통해 특정 상황에 대하여 이벤트 관리가 가능하다.
3. 이벤트 객체
    - Event.target: 이벤트가 원래 발생하였던 대상
    - Event.currentTarget: 이벤트가 발생하였던 대상
    - Event.preventDefault(): 이벤트를 취소
    - Event.stopPropagation(): 이벤트 전파 중단 
4. 이벤트 객체와 this
    - 이벤트 리스너의 콜백함수에서 this를 활용하는 경우, 이벤트 리스너에 바인딩 되어 있는 요소가 지정된다. 아래와 같이 이벤트를 등록하는 경우 버블링에 의해 this 값은 계속 변경된다.
