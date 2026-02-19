import { NextResponse } from "next/server";
import { jwtDecode } from "jose";

export function middleware(request) {
  const token = request.cookies.get("access_token")?.value;
  const { pathname } = request.nextUrl;

  // if (pathname === '/login' && token) {
  //   return NextResponse.redirect(new URL('/dashboard', request.url));
  // }

  if (pathname !== "/login" && pathname !== "/" && !token) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  const response = NextResponse.next();
  console.log("Middleware executed for path:", pathname); 

  if (token) {
    response.headers.set("x-user-token", token);
  }

  return response;
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
