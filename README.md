# Image-To-ASCII-Converter
A set of modules I wrote in python to convert an image from pixels to a representation in strings of ASCII characters.  In a process similar to image feature extraction for older computer vision approaches, we pass convolutional style filters over small 3x3 patches of pixels and flatten each local filter into its own vector.  At the same time we take each ASCII character, convert it to an image, run a similar convolution over it and convert it into a vector.  Character vectors are then compared to local pixel vectors using a minkowski distance metric, and the character that minimizes this metric is selected and appended to the string representing the image.  This approach results in a very high fidelity ASCII representation of the image with relatively few characters. 


                                                                          ,,,                                             
                                                .' ,,            ,iyeccvvcuopev<==:.,,,                                   
                                              .t- --'          .c$b%nbWWWWWWR00bbbbb0b5n>:.                               
                                              $1              =WWK7J&WWRRE%o55EE5Eh@b88WRb5gv,                            
                                             ,W[,,,         =uWWKJJ5M8PFJnh0b55080E080000WWWWo:                           
                                          ,,.=W8w:uo<=c$x===888P%J5eFJJ%4%%3FFF7????7JJ%hEWNNWWx ,                        
                                          ,JWWNWWWWWWWWRR0WRbbEEJJe%Jn3VEJJ???vvvJJJJe%%33nhE8WWo:,                       
                                        ,=c3RWWRRWMRPPPP3%353%eeeJ%%e53%eeJee%%Jv?l?veee%%3%VE%5Wg>,                      
                                     .cgbbBWWWRRWR8ZEFvvvJJ%%eeJJJJJeJJJJJJe%33%eeeJJJvvvJJe%3h5@b8;.,                    
                                  .,-{@PP0RRRRR800PE%JvvJJJJJJJvvJvJJvvJvvvJvJJe%%%%eeeeJvcvJJ%%3%Fpe=.                   
                                ' l--''"{%R80b08R0E%%JJJJJvvvvv???ll?ll?l????vvJJJJee%3hhhh%eeJ355eJIh;'                  
                                      ,,:?$@bRR0E%FeJJJJvvvvvv??llllllllllllll??vJJJJe%e%%%eeJvvJ%8&3Ip,                  
                                      c4EnJ58P%F7v??llll>>lllll>>{[[===[[[{<lllll?vvJJJJJee%%JJvv??38&Ev                  
                                   ,=o5%cn88F7v?ll><<>{{{><{{[=[{[===}}!=}}==[{{ll???JJJJJJJeeJJJvvvJ53%=                 
                                 :u$b3%nbWP%Fvl>{==}}!!====}!!!==}!!!!!!!!!=[<lll>>?c?lvJJJJeeeJJJvvvJ$5%%v,              
                              ,=o8R05b@bWP%FJvl{=}!!!!!=~!}~!!}}=}!""""""}===<{{ll??????vJJJJeeeJJv???755JvJ"'            
                            ;ipZ5h358B8W0EFJ?l[}}"""""!!!~}}!!!!!""""""""!!!!=[l?ll???l?vvJJJJJeJJ???l?JII. '':-          
                          .iogbWWWWWW0WN5EJcll=""::""""!!==!!!!!!!:::::::!::!=[[=lc?ll?llv??vJJJJ?<???vv%5o,  ''+.        
                         ,udWWWWR0WW0FNN5Fwbb&bhev<!!!!!!====!!=<<<veeeei=iil>><>{lll???ll?vvJJJl?l>vvJeJ58b=,  '"        
                        coWWNR0Ph8NRhnNWHhWWWNKFJJv=!!}!====!!=<l>l7v7hA&hh%%%l==[<ll?v?llvvJJJvl>lllvJe%%5WW&v    ',     
                       ,@dWWN0PhhW8PFJWWh3PF????l>==!!""!}!!"""}"""""^[^^^^^==}~![lll?ll>l??vJJvl==<cJJ%%3g5NWW>    '     
                       ,8WWNREh%GW8%vJ8WF7<=={{>><ll=::""""""""!!!!==!"""""""!}=={lvllll<llll?vvl>=lv7Je%55EE8NWk,        
                       ~NNWNDEgb8NW5nnWRJ<==<cvJJvvvvvi=""""":!=====lccceJvv>="!}{?Jvll><>{l<ll?l[=}{<>lJJ%555@E88v,      
                        ^PPP0hW88WR@e8WEv=<c%5%eeeJvlJEe=!""!===<lllcJ3%eJce%el==[?JJ?l>>>=llll<l{==!=<<l?J%333%%Eb>,     
                           '0@NWWN8%nWWEvl385?i@&&hFJlEWJ=!!=<=cJJJe%3Fo&&&E%FJi><lvJvlllllv?l<<{{===<?vv??J%E3%%@R8b1.   
                           .5$WWRNbv%WNFvv3Iv"dWWNhlhv3MJ>=><<lc>?JJv=>WWWN5h%Jvlll<vvl>l?vvvlll>>>>>=cvJJeeJeee%33MWWWo, 
                         -?ye08NRNWnbW0%vc%4hnn5P7?J?J8I?lllll??>lJeenn0MM0FFJvvvl<>l?llll?vv?l<l<lvJJvJJJJe%%en%58ZdNWWN.
                        '-''J$^FWWWbWWP%%hJF3VF7??vvuWWFl>lllll???7JJJJT777JJJvvJJ?>llllll?vJ?l>livJJeeJJcJJJe4V%%0W80NWWN
                           J8$' lWMFFM%F3%v???llJv?v8WP?ll?v?l?l<[={l???lll?l?JJ???><lv?vvvJJJvvvJeJJvJ48h%JJJJ%3JF0WBMNWN
                         ,v$"R[  T'  E%v?vl>=[{lv{=%WP7?l?vJJvll<=!""^{===[{{l????v?<?JvvvvJJJJvJJJ%%vlJ@JR8h%JJJJJF3R@WNW
                       ,;I^'-T' !J   JJ<=^========J8E???l??JJJvl[==}!"""""!!~^^^^!=<l?vvvvvJJ%3heJ33?{lJ%nhZ8%Fv????e%%%NN
                     ,.y]'      "1   Jy=""!!l===<c8F?>=}}=<lv%JJi!"!!!"!"""""!"""!!!l?vJvJJJn3&5J%??=!"?l%5?F5?v=>l>J%JlPN
                     1J'             JJ!!"!=[[{{=e8i=!""""![?JJJJv=""""""""""""""!!!<?veJeJJ%55%v?"}|""<l^?["55?""!!?JJ=?M
                     '               J%===<<==!!n&Wol=:":==lcv<=lJv==!""""""!!"!!!=={?ceeJJJ%33%J?!=!"=yv""":=5?-"""?JJllZ
                               ,,:;  l%llil=!""=5WWW&JcvvvJJeJJvlJ7[=<<:"""""!!====<[lceeJJe%%%%7{=l=<c=l<:"=<J['"!:[33%l0
                           ''"nb8R|  lJ?vv>!":=yc7FZM8hFJvJll<l?v?>=>=>i==!!!=<<===<[<v%%Jeeee3F^""licJ>="!<=v1-,"!=<5$Jc5
                             '-""'   lJleJ>==lcvvl>lll>>lJvl<<vl<{<ll<llvv====<<>[==[lJ%eJeJeeE?=!!yJ%JJJv=lll=.;!"yy$%c@W
                                     JJleelvi?vl?l=[ll<>ll[===l<[=<lllv?lll==[{<l===<?J3eJJJJ%F"![=cueooJJvv?>=cc:=JJ%dWWN
                                     '%lJeveecclvl=lc>==<{><l>lllvll>=<cvll?>=[>>[==lv%3%evJeVEv:=JdWWWWpccccc@W&uhdWWNNNN
                                      ?Jve?73hhgeJcvecevJeJcvJJJJeJccilll>ll<>=<<>><?JeV%vvJ%3WWWNWWNNNNNNNNWWWWNWWWNNNNNN
                                      '%y%c[?%$WWWWW0R0b0R0@b5%%%55ow@oJvl>ll=>l<<lllv%Evlvn%dNNNNNNNNNNNNNNNNNNNNNNNNNNNN
                                       "JJEl"^lF08WP33%FFE3%%JJJe%@WWWKFFliJ>=ll>[[[<cET>lc3&WNNNNNNNNNNNNNNNNNNNNNNNNNNNN
                                   ,,;=a5l?%=!={l887JJJ?JJJJvJJvJn0NRF7?>?Jv=>?l[==={JF[=c@WNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
                            ,;<udWWWWNNNNk=?e="!}WW?l?vvJJJJe%?le$5%FJ<^!<Jl=>?<}~}=lJ==gWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
                        ,=uWWWNNNNNNNNNNNN&=vJ""!8Wv=l??vJJeeJ>c55F%Jl====ll~l?}!!==c=uWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNR
                   .<o&WWWNNNNNNNNNNNNNNNNNR=F<"!TW%={<lvJJe%vl3Z%%J<[?{!!!=!vl""!<u3WWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMWRP
                .uWWWWNNNNNNNNNNNNNNNNNNNNNN&>%=!?W&>==lJvJ%elJ5FJ?>{{=!!"""=?^"=cWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNR80b5
                WWWWNNNNNNNNNNNNNNNNNNNNNNNNN&Jo==MWk<=lJvJevJV%?l{}!!"""""!l""=dWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNR000885
                NWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWo>lWWh>>JcJveE7[=!!!"""""":=!<dWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNRPEhZ5Z05
                WWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNN&clWWbcclce%?^!!~}!""""""<uWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKPhh50bEb50
                WWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNoi8WWRbEF^""!!"!"""":idWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNR0bb@58550G0W
                WWWNWRMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWJJ%F?=""!!!:""""<gWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNM0bb5@580EEZ88W
                WWWNWBWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN&Fc>>==<li<=loWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNM85hE35555bb8WWN




