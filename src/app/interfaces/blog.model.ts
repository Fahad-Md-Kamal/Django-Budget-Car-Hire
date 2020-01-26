import { User } from './User.model';
import { BlogTopic } from './BlogTopic.model';

export interface Blog {
    user: User;
    title: string;
    content: string;
    topic: BlogTopic;
    image: string;
    posted_on: Date;
    updated_on: Date;
    approved_by: User;
    is_approved: boolean;
}