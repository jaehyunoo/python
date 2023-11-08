'''
    작성일 : 2023년 11월 8일
    작성자 : 컴소부 202095061 유재현
    설명 : LAB 8-3 (P.210)
'''

partyA = set(["Park","Kim","LEE"])
partyB = set(["Park","Choi"])


print("2개의 파티에 모두 참석한사람 :  ", partyA.intersection(partyB)) # A,B파티를 모두 참석한사람 => 교집합 메소드 .intersection()
print("파티 A, B에 참석한 사람 :  ", partyA.union(partyB))  # A,B를 참석한사람을 중복되지 않도록 출력 => 합집합 메소드 .union()
print("파티 A, B에 중복없이 참석한 사람 :  ", partyA.symmetric_difference(partyB)) # A B중 한군데만 참석한사람 => 대칭차집합 메소드 .symmetric_difference()
print("파티 A만 참석한 사람 :  ", partyA.difference(partyB)) # A에만 참석한사람 => 차집합 메소드 .difference()