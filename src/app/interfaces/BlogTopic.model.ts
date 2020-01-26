import { User } from './User.model';

export interface BlogTopic {
    topic: string;
    description: string;
    created_by: User;
    updated_by: User;
    created_on: Date;
    updated_on: Date;
}