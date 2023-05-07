#include <jni.h>
#include <string.h>

int key[] = {0, 0, 0, 0, 0, 0, 11, 126, 48, 99, 89, 7, 27, 30, 39, 23, 28, 100, 54, 21, 10, 26, 103, 64, 10, 55, 41, 7, 0, 0};

extern "C" JNIEXPORT jboolean JNICALL Java_com_example_noteasydroid_MainActivity_check(JNIEnv* env, jobject obj, jstring str) {
    jbyte buffer[1024];
    const char *p = env->GetStringUTFChars(str, 0);
    int len = strlen(p);
    for (int i = 0; p[i] && i < 30; i++)
        buffer[i] = p[i] ^ key[i];
    jbyteArray ba = env->NewByteArray(len);
    env->SetByteArrayRegion (ba, 0, len, buffer);
    jclass clazz = env->GetObjectClass(obj);
    jmethodID check = env->GetMethodID(clazz, "check", "([B)Z");
    return env->CallBooleanMethod(obj, check, ba);
}