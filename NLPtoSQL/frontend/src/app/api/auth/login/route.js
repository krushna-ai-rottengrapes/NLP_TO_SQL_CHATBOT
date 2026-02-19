import {NextResponse} from "next/server";

export async function POST(request) {
  try {
    const {username, password} = await request.json();
    console.log(process.env.NEXT_PUBLIC_API_URL);
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/users/login`,
      {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password}),
      }
    );
    console.log(response);
    if (!response.ok) {
      const error = await response.json();
      console.log(error);
      return NextResponse.json(
        {error: error.detail || "Login failed"},
        {status: response.status}
      );
    }

    const data = await response.json();
    const res = NextResponse.json({user: data.user, client: data.client});

    res.cookies.set("access_token", data.access_token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "strict",
      maxAge: 86400,
      path: "/",
    });

    return res;
  } catch (error) {
    console.log(error);
    return NextResponse.json({error: "Login failed"}, {status: 500});
  }
}
