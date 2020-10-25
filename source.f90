program chipper !start (this is Fortran 90 code, don't try to compile as something else!)

    implicit none  ! removing that weird thing FORTRAN does with implicit types
    real :: chips, hamburgers, total,&  !casting numbers as floats
    chips_cost = 0.30, hamburgers_cost = 0.40, chips_price = 0.75, hamburgers_price = 0.95
    character (len = 32)  :: str = "euro in profit total",&  ! defining strings
    str2 = "euro in profit on chips", str3 = "euro in profit burgers"
11  format (A8, F16.2,"    ", A32)  ! make a format with label 11

    print*, "********************"
    print*, "profit calculator"
    print*, "********************"
    print "(A,$)", "enter chips sold: "
    read*, chips  ! input for chips
    print "(A,$)", "enter burgers sold: "
    read*, hamburgers  ! input for burgers

    chips = chips * (chips_price - chips_cost)  ! profit on chips
    hamburgers = hamburgers * (hamburgers_price - hamburgers_cost)  ! profit on burgers
    total = chips + hamburgers  ! total profit

    write (*,11) "you made", total, adjustl(str)
    write (*,11) "you made", chips, adjustl(str2)
    write (*,11) "you made", hamburgers, adjustl(str3)

end program chipper !end
