export interface User {
    email: string;
    username: string;
    first_name: string;
    last_name: string;
    is_owner: boolean;
    is_staff: boolean;
    image: string;
    timestamp: Date;
}