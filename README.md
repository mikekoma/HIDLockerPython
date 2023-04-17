# Title

Seeduino XIAO HID1Switch Locker


# Overview

Lock your desktop with one switch.


# Description

## Hardware

Seeduino XIAO SAMD21
[Seeed Studio XIAO SAMD21(Seeeduino XIAO) - Arduino Microcontroller - SAMD21 Cortex M0+ with Free Course - 5V/16MHz](https://www.seeedstudio.com/Seeeduino-XIAO-Arduino-Microcontroller-SAMD21-Cortex-M0+-p-4426.html)

>   配線図
>    
>    +-------SW--------+
>    |  _____________  |
>    +--D0   USB   5V  |
>       D1        GND--+
>       D2        3V3
>       D3        D10
>       D4         D9
>       D5         D8
>       D6_________D7


## Software

### スイッチ押した時
Shiftキー送信(スクリーンセーバー解除)

### スイッチ離した時
Win+Lキー送信(画面ロック)

### 制限
キー送信した後、1秒間はスイッチの変化検出を行わない。

# Licence

MIT License

Copyright (c) 2023 Suns & Moon Laboratory

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# Author

Suns & Moon Laboratory  
https://www.s-m-l.org  
https://github.com/mikekoma/  
https://twitter.com/mikekoma  
