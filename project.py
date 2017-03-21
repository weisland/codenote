    g Xoo f.lst > f1.lst
    paste f1.lst  f1.lst > cmp1.lst
    paste f2.lst  f2.lst > cmp2.lst
    perl -ane 'if($F[1] ne $last){print "$F[1],"}$last=$F[1];'  cmp2.lst
    perl -ane 'if($F[1] ne $last){print " cuff_$F[0]/abundances.cxb"}else{print ",$F[0]_out/abundances.cxb"};$last=$F[1];' cmp2.lst
