#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Apr 28, 2020 12:40:42 PM +0300  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 600x450+365+234
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra43 \
        -borderwidth 2 -relief groove -background #89c99f -height 345 \
        -width 515 
    vTcl:DefineAlias "$top.fra43" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra43
    label $site_3_0.lab44 \
        -background #89c99f -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 72 -weight bold} -foreground #ffffff 
    vTcl:DefineAlias "$site_3_0.lab44" "answer_Label" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -background #89c99f -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 19 -weight bold} -foreground #ffffff 
    vTcl:DefineAlias "$site_3_0.lab46" "userScore_Label" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black -background #89c99f \
        -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 19 -weight bold} -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_3_0.lab50" "opponentScore_Label" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #ffffff \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 14 -weight bold} -foreground #89c99f \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -takefocus 0 -text {play again} 
    vTcl:DefineAlias "$site_3_0.but51" "playAgain_Button" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 14 -weight bold} -foreground #89c99f \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -takefocus 0 -text close 
    vTcl:DefineAlias "$site_3_0.but52" "close_Button" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab44 \
        -in $site_3_0 -x 40 -y 50 -width 454 -relwidth 0 -height 121 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 140 -y 160 -width 224 -relwidth 0 -height 71 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 130 -y 210 -width 224 -relwidth 0 -height 71 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 80 -y 310 -width 107 -relwidth 0 -height 64 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but52 \
        -in $site_3_0 -x 360 -y 310 -width 107 -height 64 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra43 \
        -in $top -x 40 -y 20 -width 523 -relwidth 0 -height 403 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

