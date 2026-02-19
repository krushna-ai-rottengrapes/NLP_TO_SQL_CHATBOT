import {NextResponse} from "next/server";

export async function GET(request) {
  try {
    const token = request.cookies.get("access_token")?.value;

    if (!token) {
      return NextResponse.json({error: "Not authenticated"}, {status: 401});
    }

    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/users/me`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!response.ok) {
      return NextResponse.json(
        {error: "Failed to fetch user"},
        {status: response.status}
      );
    }

    const data = await response.json();
    return NextResponse.json({user: data.user, client: data.client, token});
  } catch (error) {
    return NextResponse.json({error: "Failed to fetch user"}, {status: 500});
  }
}
