/ * 
 * This program and the accompanying materials are made available under the terms of the 
 * Eclipse Public License v2.0 which accompanies this distribution , and is available at 
 * https://www.eclipse.org/legal/epl-v20.html 
 * 
 * SPDX - License - Identifier : EPL-2.0 
 * 
 * Copyright Contributors to the Zowe Project . 
 * 
 * / 

 / * * 
  * Interface for payload to cancel a job . 
  * @export 
  * @interface ICancelJob 
  * / 
 export interface ICancelJob { 

     / * * 
      * " cancel " is currently the only valid value 
      * @type { string } 
      * @memberof ICancelJob 
      * / 
     request : string ; 

     / * * 
      * Version , at the time of writing , 1.0 or 2.0 are accepted . 
      * @type { string } 
      * @memberof ICancelJob 
      * / 
     version : string ; 
 } 
