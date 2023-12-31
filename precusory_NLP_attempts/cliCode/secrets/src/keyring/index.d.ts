/* tslint:disable */
/* eslint-disable */

/* auto-generated by NAPI-RS */

export interface Credential {
  account: string
  password: string
}
export function deletePassword(service: string, account: string): Promise<boolean>
export function findCredentials(service: string): Promise<Array<Credential>>
export function findPassword(service: string): Promise<string | null>
export function getPassword(service: string, account: string): Promise<string | null>
export function setPassword(service: string, account: string, password: string): Promise<void>
