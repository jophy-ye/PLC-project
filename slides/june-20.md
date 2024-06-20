# June 20 Meeting

Weekly check-in with Michael. I'll mainly present various PLC code sources.

I adopted a BFS on the sources, though Wojciech probably wants me to do DFS. That said, the following list isn't yet complete; some are still tabs (on my browser) to be parsed.


## Misc
- <details>
  <summary>Open-source formal verification tool developed for their PLC</summary>

  ![Add](https://cdn.prod.website-files.com/63dea6cb95e58cb38bb98cbd/6415da00f4c83f3bd7f0d8bf_5e58720d2804b2490a9b2438_Screen-Shot-2018-10-02-at-9.09.00-PM.png)
  ![Add & timer](https://cdn.prod.website-files.com/63dea6cb95e58cb38bb98cbd/6415da00f4c83f7c3af0d8be_5e58720df68ab8d231a6af8f_Screen-Shot-2018-10-02-at-9.09.19-PM.png)
  </details>


## Code Libraries
- 💾 [Rockwell Automation Sample Code Library](https://www.rockwellautomation.com/en-us/support/product/product-downloads/application-code-library/sample-code.html)
    - .exe, only accessible with their Studio 5000? Nope!
- 💾 [Siemens Open Library](https://openplclibrary.com/), developed with DMC.
    - Access through [Siemens TIA Portal](https://www.siemens.com/global/en/products/automation/industry-software/automation-software/tia-portal/highlights/tia-portal-cloud.html)?
    - Can we look into the code?
- 💾 [Omron Sample Code Library](https://automation.omron.com/en/us/support/resources/sample-code/)
    - Haven't looked too deep into it
- 💾 [Kollmorgen PLC Standard Library](https://webhelp.kollmorgen.com/kas4.01/Content/11.TechRefs/PLC-Standard/_OVRVW-PLC-Standard-Libraries.htm?tocpath=Technical%20References%7CProgramming%20Languages%7CPLC%20Standard%20Libraries%7C_____0)
    - Haven't looked too deep into it
- 💾 Ladder logic + Arduino [repo](https://github.com/cpipero/ArduinoLadder) ([another one](https://github.com/wditch/plcLib/tree/master/examples), though in Arduino language)


## Software
- [Simulink PLC coder](https://www.mathworks.com/help/plccoder/index.html?s_tid=CRUX_lftnav) from Mathworks, *free access for us*


## Courses
- RealPars for Siemens


## Less Important Misc
- Cute [article](https://www.controldesign.com/displays/hmi/article/11309970/open-source-plc-and-hmi-library-makes-headway) on DMC's view on open-sourcing PLC code and their collab with Siemens. Another [one](https://www.dmcinfo.com/latest-thinking/case-studies/view/id/273/mitsubishi-plc-standard-library) with Mitsubishi here.
- [IEEE paper](https://www.researchgate.net/publication/4278362_A_Study_of_Industrial_Logic_Control_Programming_using_Library_Components) on some observations (using function blocks, code for things other than automation) in the automobile industry.
- [Siemens TIA Portal tutorial](https://www.solisplc.com/tutorials/working-with-libraries-in-siemens-tia-portal-plc-programming)