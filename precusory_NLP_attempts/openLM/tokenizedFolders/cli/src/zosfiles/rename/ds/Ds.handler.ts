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

 import { AbstractSession , IHandlerParameters } from " @zowe / imperative " ; 
 import { ZosFilesBaseHandler } from " .. / .. /ZosFilesBase.handler " ; 
 import { Rename , IZosFilesResponse } from " @zowe / zos - files - for - zowe - sdk " ; 

 / * * 
  * Handler to rename a data set 
  * / 
 export default class DsHandler extends ZosFilesBaseHandler { 
     public async processWithSession(commandParameters : IHandlerParameters , session : AbstractSession ): Promise < IZosFilesResponse > { 
         const { beforeDataSetName , afterDataSetName } = commandParameters.arguments ; 
         return Rename.dataSet(session , beforeDataSetName , afterDataSetName ) ; 
     } 
 } 
