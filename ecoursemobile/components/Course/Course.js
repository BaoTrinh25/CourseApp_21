import {View, Text, ActivityIndicator} from "react-native";
import MyStyles from "../../styles/MyStyles";
import React from "react";
import APIs, { endpoints } from "../../configs/APIs";
import { Chip } from "react-native-paper";

const Course = () => {
    const [categories, setCategories] = React.useState(null);
    const [courses, setCourses] = React.useState([]);
    const [loading, setLoading] = React.useState(false);

    const loadCates = async () => {
        try {
            let res = await APIs.get(endpoints['category']);
            setCategories(res.data);
        }catch (ex) {
            console.error(ex);
        }
    }


    const loadCourses = async () => {
        try {
            setLoading(true);
            let res = await APIs.get(endpoints['course']);
            setCourses(res.results.data);
        }catch (ex) {
            console.error(ex);
        } finally {
            setLoading(false);
        }
    }

    React.useEffect(() => {
        loadCates();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>DANH MỤC KHÓA HỌC</Text>
            <View style={MyStyles.row}>
            {categories==null?<ActivityIndicator />:<>
                {categories.map(c => <Chip style={MyStyles.margin} key={c.id} icon="shape">{c.name}</Chip>)}
            </>}
            </View>
        </View>
    )
}

export default Course;