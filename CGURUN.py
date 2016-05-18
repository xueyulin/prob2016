from turtle import *

def main():
    reset()


    #頭
    #頭左側
    width(1)
    up()
    goto(-5,-37)
    left(200)
    down()
    color("black","black")
    begin_fill()
    circle(55,90)
    up()
    left(15)
    down()
    circle(35,140)
    #頭底第一個角
    up()
    right(0)
    circle(18,270)
    down()
    circle(18,90)
    #上弧 右
    up()
    circle(18,270)
    down()
    left(40)
    circle(40,48)
    #上弧 左
    up()
    right(166)
    circle(17,272)
    down()
    circle(17,95)
    #第二個角
    up()
    circle(17,265)
    right(23)
    down()
    circle(50,29)
    #最上面的角
    #上弧 左
    up()
    left(30)
    circle(50,335)
    down()
    circle(50,25)
    #上弧 右
    up()
    circle(50,335)
    right(150)
    down()
    circle(53,48)
    #下勾
    up()
    right(27)
    circle(45,284)
    down()
    circle(45,76)
    
    
    
    #rUn
    up()
    goto(165,-167)
    down()
    width(1)
    color("black","white")
    begin_fill()
    goto(212,-216)
    goto(291,-190)
    goto(294,-125)
    goto(242,-141)
    goto(260,-167)
    goto(220,-180)
    goto(220,-147)
    goto(165,-167)
    end_fill()

    #ruN
    up()
    goto(308,-119)
    down()
    width(1)
    color("black","white")
    begin_fill()
    goto(350,-105)
    goto(365,-125)
    goto(383,-94)
    goto(382,-161)
    goto(338,-175)
    goto(326,-152)
    goto(304,-183)
    goto(308,-119)
    end_fill()
    
    
    #右手肩膀開始
    up()
    goto(70,-90)
    down()
    width(1)
    color("black","white")
    begin_fill()
    goto(150,-90)
    goto(159,-96)
    #右手關節
    goto(164,-100)
    goto(160,-109)
    #前手臂
    goto(102,-180)
    #右腿
    goto(210,-231)
    goto(393,-168)
    goto(215,-264)
    #左腿
    goto(102,-249)
    goto(39,-264)
    goto(118,-300)
    goto(-6,-282)
    goto(-17,-278)
    goto(-24,-270)
    goto(-27,-264)
    goto(-23,-251)
    goto(-19,-239)
    goto(-11,-233)
    goto(-4,-229)
    #腰
    goto(32,-216)
    goto(-2,-185)
    #左手
    goto(-4,-216)
    goto(-8,-220)
    goto(-15,-225)
    goto(-30,-225)
    goto(-96,-171)
    goto(-36,-202)
    goto(-37,-155)
    #肩膀
    goto(-35,-151)
    goto(-31,-147)
    goto(-26,-142)
    goto(-15,-138)
    goto(5,-134)
    goto(12,-130)
    goto(18,-126)
    goto(23,-118)
    goto(29,-110)
    goto(42,-101)
    goto(54,-94)
    goto(60,-92)
    goto(70,-90)
    end_fill()
    #右手空隙
    up()
    goto(68,-125)
    down()
    width(1)
    color("black","white")
    begin_fill()
    goto(92,-178)
    goto(94,-177)
    goto(124,-121)
    goto(125,-119)
    goto(121,-118)
    goto(68,-125)
    up()
    goto(390,-291)
    end_fill()

    
    


if __name__ == '__main__':
    main()
    mainloop()
