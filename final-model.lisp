
(clear-all)

(define-model final

(sgp :v nil :esc t :lf .1 :bll 0.5 :ans 0.4 :rt 0.2 :show-focus t :ul t :ult t :needs-mouse t)

(chunk-type goal state count target)
(chunk-type learned-info item location)

(start-hand-at-mouse)
(set-visloc-default screen-x lowest)

(add-dm
 (goal isa goal)
 (attending) (read) (encode))


(p ready
   =goal>
      ISA         goal
      state       nil
   =visual-location>
   ?visual>
       state      free
==>
   =goal>
      state       read-target
    +visual>
      cmd        move-attention
      screen-pos =visual-location
)

(p read-target
   =goal>
      ISA         goal
      state       read-target
   =visual>
     ISA         visual-object
     value       =char
   ?imaginal>
     buffer      empty
     state       free 
==>
   =goal>
      state       remember
      target      =char
   +imaginal>
      isa     learned-info
      item    =char
   +retrieval>
      isa     learned-info
      item    =char

)

(p remember-loc
   =goal>
     ISA   goal
     state remember
   =retrieval>
      isa   learned-info
      item  =char
      location  =loc
==>
  +visual>
     isa move-attention
     screen-pos =loc
  @retrieval>
  =goal>
   state    match
)

(p successful-match 
   =goal>
     ISA goal
     state match
     target =tar
  =visual>
   value =tar
   screen-pos =loc	
  ?manual>
      state      free
  =imaginal>
  ==>
  +manual>
      isa        move-cursor
      object     =visual
  =imaginal>
      isa     learned-info
      location    =loc
  -imaginal>
  =goal>       
  state click-mouse
) 

(p click-mouse
   =goal>
       state  click-mouse
   ?manual>
      state  free
  ==>
   =goal>
       state  nil
   +manual>
      isa    click-mouse)

(p no-match
   =goal>
     ISA goal
     state match
     target =tar
  =visual>
   -  value =tar
==>
  =goal>
     state       reading
)


(p cant-remember-loc
     =goal>
       ISA goal
       state remember
     ?retrieval>
       buffer  failure
    ==>
     =goal>
       state reading
)


(p read-item
    =goal>
      isa       goal
      state     reading
   ==>
    +visual-location>
      isa       visual-location
      kind      oval
      > screen-y current
      screen-y  lowest
    =goal>
      state     attending)

(p attend
    =goal>
      isa     goal
      state   attending
    =visual-location>
    ?visual>
      state   free
   ==>
    =goal>
      state      match
    +visual>
      cmd        move-attention
      screen-pos =visual-location)

(goal-focus goal)

 )



